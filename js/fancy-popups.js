var isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints>0) || (navigator.msMaxTouchPoints > 0);

//all top-level popup objects must go into this array
var registeredPopups = new Array(); //keep track of popups

/************ POPUP BASE CLASS ************/

// Popup constructor
var Popup = function(refpatt,id)
{
    this.refpatt = refpatt; //pattern to select references
    this.id = id;           //id of popup div

    this.ref = null;    //reference element
    this.href = null;   //id of target element
    this.tgt = null;    //target element

    this.pudiv = null;  //popup div

    this.isrendered = false;

    this.timeout = false;
    this.delay = false;

    this.registerSafe();
}

// concealRenderedPopups (class) helper function
Popup.concealRenderedPopups  = function()
{
    $.each(registeredPopups, function(index, thepopup) {
        if (thepopup.isrendered)
        {
            thepopup.concealImmediate();
            return;
        }
    });
}

// reregisterPopups (class) helper function
Popup.reregisterPopups = function()
{
    $.each(registeredPopups, function(index, thepopup) {
        thepopup.register();
    });
}

//reference UI event handlers
Popup.prototype.refevent = function(ref)
{
    this.ref = $(ref);
    this.href = this.ref.attr('href');
    this.tgt = this.target(this.href);
    return this;
}
Popup.prototype.refclick = function(e)      {e.data.thispopup.refevent(this).reveal();}
Popup.prototype.refmouseenter = function(e) {e.data.thispopup.refevent(this).reveal();}
Popup.prototype.refmouseleave = function(e) {e.data.thispopup.conceal();}

//popup UI event handlers
Popup.prototype.puclick = function(e)      {e.data.thispopup.conceal();}
Popup.prototype.pumouseenter = function(e) {e.data.thispopup.keepvisible();}
Popup.prototype.pumouseleave = function(e) {e.data.thispopup.conceal();}

Popup.prototype.register = function()
{
    clearTimeout(this.timeout);
    clearTimeout(this.delay);
    if (this.isrendered)
        this.concealImmediate();
}

Popup.prototype.registerHandlers = function()
{
    var refs = $(this.refpatt);
    refs.off();
    this.pudiv.off();
    if(isTouchDevice)
    {
        refs.on('click', {thispopup:this}, this.refclick);
        this.pudiv.on('click', {thispopup:this}, this.puclick);
    }
    else
    {
        refs.on('mouseenter', {thispopup:this}, this.refmouseenter);
        refs.on('mouseleave',  {thispopup:this}, this.refmouseleave);

        this.pudiv.on('mouseenter', {thispopup:this}, this.pumouseenter);
        this.pudiv.on('mouseleave', {thispopup:this}, this.pumouseleave);
    }
    refs.removeClass('disabled');
}

Popup.prototype.getpopupdiv = function()
{
    if ($(this.id).length == 0)
    {
        this.pudiv = $(document.createElement('div')).attr('id',this.id.substr(1));
        $(document.body).append(this.pudiv);
    }
    else
        this.pudiv = $($(this.id)[0]); //used only by transcript popups

    this.hide();
}

Popup.prototype.registerSafe = function(dontneedMathJax)
{
    var thispopup = this;
    $(document).ready( function()
    {
        var tgts = $(thispopup.refpatt);
        if (!tgts.length)
        {
            registeredPopups = registeredPopups.filter(function(currentValue){
                return currentValue != thispopup;
            });
            delete thispopup;
            return;
        }

        $(thispopup.refpatt).addClass('disabled');

        thispopup.getpopupdiv();

        if (dontneedMathJax || typeof MathJax == 'undefined')
        {
             thispopup.register();
             thispopup.registerHandlers();
        }
        else
            MathJax.Hub.Queue(function () {
                thispopup.register();
                thispopup.registerHandlers();
            });
    });
}

Popup.prototype.target = function(href)
{
    return  $(href); //this usually works, but needs to be over-ridden in several cases
}

Popup.prototype.render = function()
{
    var tgtclass = this.tgt.attr('class');
    this.pudiv.addClass(tgtclass + (isTouchDevice ? ' mobile' : ''));

    return true; //NOTE: render method must return true or there will be no popup
}

//Popup.prototype.position = function() { /* virtual */ }

Popup.prototype.revealImmediate = function()
{
    clearTimeout(this.timeout);
    this.pudiv.stop(true);

    this.isrendered = this.render();

    if (this.isrendered) //NOTE: render method must return true or there will be no popup
    {
        this.position();
        this.show();
    }
}

Popup.prototype.reveal = function()
{
    if(isTouchDevice)
    {
        this.pudiv.stop(true);

        if (this.isrendered)
        {
            if (this.href == this.pudiv.attr('href'))
            {
                this.conceal();
                return;
            }
        }
        else
            Popup.concealRenderedPopups();

        this.revealImmediate();
    }
    else
        this.delay =
            setTimeout(function(thispopup)
            {
                Popup.concealRenderedPopups(); //######
                thispopup.revealImmediate();
            },
            175,this);
}

Popup.prototype.concealImmediate = function()
{
    this.hide();
    this.isrendered = false;
}

Popup.prototype.conceal = function()
{
    clearTimeout(this.delay);
    this.pudiv.stop(true);

    if (!this.isrendered)
        this.concealImmediate();
    else
        this.timeout = setTimeout(
            function(thispopup) {
                thispopup.pudiv.animate(
                    { opacity: 0 },
                    {
                        duration: 250,
                        complete: function() { thispopup.concealImmediate() },
                        fail:     function() { thispopup.pudiv.css('opacity','') }
                    }
                );
            },
            100,this
        );
}

Popup.prototype.keepvisible = function()
{
    clearTimeout(this.timeout);
    this.pudiv.stop(true)
    this.show();
}

Popup.prototype.hide = function()
{
    this.pudiv.attr('class','concealed popup').stop(true).removeAttr('style');
}

Popup.prototype.show = function()
{
     this.pudiv.removeClass('concealed').addClass('revealed');
}

Popup.prototype.scrollto = function()
{
    if (this.isrendered)
        this.pudiv.css('pointer-events','none');

    this.sendGAevent("Scroll",this.href,1);
}

function functionName(fun) {
  var ret = fun.toString();
  ret = ret.substr('function '.length);
  ret = ret.substr(0, ret.indexOf('('));
  return ret;
}
Popup.prototype.sendGAevent = function(action,href,value)
{
    var filepath = window.location.pathname;
    var filename = filepath.slice(filepath.lastIndexOf("/")+1);
    var filename = filename.slice(0,filename.indexOf("."));

    var shref = href.replace(/(Ch\d+\-|mjx\-eqn\-|I+)/g,"").replace("#",":");

    if (shref.indexOf('Eq')>-1)
    {
        var filenum = filename.replace(/I+_0*/,"");
        shref = shref.replace(filenum,"");
    }

    var constructorname = typeof this.constructor.name !== 'undefined' ? this.constructor.name : functionName(this.constructor);
}

/************ POPUP HIGHPOP SUBCLASS ************/

// Highpop constructor
function Highpop(refpatt,id)
{
    Popup.call(this,refpatt,id); // Call  parent constructor

    this.revealTime = false;
}

//make Highpop prototype that inherits from Popup prototype
Highpop.prototype = Object.create(Popup.prototype);

// Set the "constructor" property to refer to Highpop
Highpop.prototype.constructor = Highpop;

// override the "register" method
Highpop.prototype.register = function()
{
    Popup.prototype.register.call(this); //call parent method
}

Highpop.prototype.registerHandlers = function()
{
    Popup.prototype.registerHandlers.call(this); //call parent method

    var thispopup = this;
    $(this.refpatt).each(function()
    {
        var href = $(this).attr('href');
        var tgt = thispopup.target(href);

        if(tgt.offset()!=undefined)
        {
            if (isTouchDevice)
                $(this).off('taphold').on('taphold', {thispopup:thispopup}, thispopup.reftaphold);
            else
                $(this).off('click').on('click', {thispopup:thispopup}, thispopup.refclick);
        }
        else
             $(this).off('mouseenter').off('mouseleave').off('click').off('taphold').addClass('badlink'); //make bad links red
    });

    if (isTouchDevice)
        this.pudiv.on('taphold', {thispopup:this}, this.putaphold);
    else
        this.pudiv.on('click', {thispopup:this}, this.puclick);
}

Highpop.prototype.completelyVisible = function()
{
    return (this.tgt.offset().top + parseFloat(this.tgt.css('border-top-width')) >= $(window).scrollTop()) &&
         ($(window).scrollTop()+$(window).height() > this.tgt.offset().top + this.tgt.height());
}

// override the "render" method
Highpop.prototype.render = function()
{
    if (!this.completelyVisible())
    {
        Popup.prototype.render.call(this); //call parent method

        if (this.href != this.pudiv.attr('href'))
            this.pudiv.html(this.tgt.html()).attr('href',this.href).find("*[id]").removeAttr("id");
        this.pudiv.css('font-size',0.75*parseFloat(this.tgt.css('font-size')));
        return true;
    }
    else
    {
        this.tgt.css({
            'transition':'none',
            'background':'#ff9',
        });
        return false;
    }
}

//override the "conceal" method
Highpop.prototype.conceal = function()
{
    Popup.prototype.conceal.call(this); //call parent method

    if( !this.isrendered )
    {
        this.tgt.stop(true,true).css({
            'transition':'background .3s linear 0s',
            'background':'#fff'
        });
    }
}

Highpop.prototype.revealEvent = function()
{
    if (this.revealTime != false)
    {
        this.sendGAevent(
            this.isrendered?"Popup":"Hilite",
            this.href,
            ((new Date).getTime() - (this.revealTime).getTime())/10
        );
        this.revealTime = false;
    }
}

Highpop.prototype.concealImmediate = function()
{
    this.revealEvent();

    if (this.isrendered)
    {
        Popup.prototype.concealImmediate.call(this); //call parent method

        //restore click method after (possibly) preventing bouncing in puclick method
        this.pudiv.off('click', {thispopup:this}, this.puclick); //in case not
        this.pudiv.on('click', {thispopup:this}, this.puclick);
    }
}

Highpop.prototype.revealImmediate = function()
{
    this.revealEvent();
    this.revealTime = new Date;

    Popup.prototype.revealImmediate.call(this); //call parent method
}

// override the ".scrollto" method
Highpop.prototype.scrollto = function()
{
    Popup.prototype.scrollto.call(this);
    this.revealEvent();
}

//override the puclick event handler
Highpop.prototype.puclick = function(e) {

    e.stopImmediatePropagation();

    var thispopup = e.data.thispopup;

    thispopup.conceal();

    if (e.target.localName == "a") return; //let links go where they may

    if (!isTouchDevice)
    {
        // prevent bouncing from extra clicks!
        $(this).off('click', thispopup.puclick);

        try { history.pushState(null,'',thispopup.href); } catch(e) {}
        thispopup.scrollto();
        return false; //prevent browser default action
    }
 }

//override the refclick event handler
Highpop.prototype.refclick = function(e)
{
    e.preventDefault();

    var thispopup = e.data.thispopup;

    thispopup.refevent(this);

    if (thispopup.completelyVisible())
    {
        Popup.concealRenderedPopups();

        thispopup.tgt.css({
            'transition':'none',
            'background':'#ff9',
         });
        thispopup.tgt.animate({
            backgroundColor: isTouchDevice? '#ff0' :'#884',
            color: isTouchDevice? '#000':'#fff'
        }, 250, "linear", function() {
            thispopup.tgt.css({
                'transition': 'background .25s linear 0s, color .25s linear 0s',
                'background': isTouchDevice? '#fff' : '#ff9',
                'color': '#000'
            });
        });
        thispopup.sendGAevent("Wink",thispopup.href,1);
    }
    else
    {
        thispopup.reveal();
        if(!isTouchDevice)
        {
            try { history.pushState(null,'',thispopup.href); } catch(e) {}
            thispopup.scrollto();
            thispopup.conceal();
        }
    }
}

Highpop.prototype.putaphold = function(e)
{
    var thispopup = e.data.thispopup;

    if (e.target.localName != "a") //let links go where they may
    {
        try { history.pushState(null,'',thispopup.href); } catch(e) {}
        thispopup.scrollto();
    }
    thispopup.conceal();
    return false; //prevent browser default action
 }

Highpop.prototype.reftaphold = function(e)
{
    var thispopup = e.data.thispopup;

    thispopup.refevent(this);

    if (!thispopup.completelyVisible())
    {
        if (!thispopup.isrendered)
        {
            Popup.concealRenderedPopups();
            thispopup.revealImmediate();
        }

        try { history.pushState(null,'',thispopup.href); } catch(e) {}
        thispopup.scrollto();

        if (thispopup.isrendered)
            thispopup.conceal();
    }
    return false; //prevent browser default action
}

/************ HIGHPOP HIPOPFOOTNOTE SUBCLASS ************/

//HighpopFootnote constructor
function HighpopFootnote()
{
    Highpop.call(this, "a[id^='footnote_source']","#footnotediv","footnote"); // Call  parent constructor
}

//make HighpopFootnote prototype that inherits from Highpop prototype
HighpopFootnote.prototype = Object.create(Highpop.prototype);

// Set the "constructor" property to refer to HighpopFootnote
HighpopFootnote.prototype.constructor = HighpopFootnote;

// override the "target" method
HighpopFootnote.prototype.target = function(href)
{
    var id = href.substr(1);
    return $('a[id=' + id + ']').parent();
}

HighpopFootnote.prototype.position = function()
{
    var refoffset = this.ref.offset();
    // This should be whatever the main id of youdoc is
    var doc = $("#EssayContentsInner");
    var docleft = doc.offset().left + parseFloat(doc.css('padding-left'));
    var docright = docleft + doc.width();
    var maxleft = docright - this.pudiv.outerWidth(true);

    var left = refoffset.left + 10;
    if(left > maxleft) left = Math.max(maxleft,docleft);

    this.pudiv.css({
        'left':left,
        'max-width': docright - left,
        'height':''
    });

    var puheight = this.pudiv.outerHeight(true);

    var winheight = $(window).height();
    var winscrolltop = $(window).scrollTop();

    var hightop = refoffset.top - puheight - 10;
    var lowtop = refoffset.top + this.ref.outerHeight(true)+10;
    var top;

    if(lowtop + puheight + 20   <=  winscrolltop + winheight)
        top = lowtop;
    else if ( (hightop >= winscrolltop) && (hightop + puheight <=  refoffset.top) )
        top = hightop;
    else
        top = winscrolltop;

    this.pudiv.css('top',top-winscrolltop);
    if (puheight >= winheight)
        this.pudiv.css('height',winheight - 20);
}

// override the "render" method
HighpopFootnote.prototype.render = function()
{
    var isrendered = Highpop.prototype.render.call(this); //call parent method

   if(isrendered)
        this.pudiv.css('max-width','none').find('a:empty,a[href*=footnote]').remove();

    return isrendered;
}

// override the ".scrollto" method
HighpopFootnote.prototype.scrollto = function()
{
    Highpop.prototype.scrollto.call(this);
    window.scrollTo(0, this.tgt.offset().top + this.tgt.outerHeight(true) - $(window).height());
}

registeredPopups.push(new HighpopFootnote());


    var hidden, visibilityChange; //Visibility API compatibility
    if (typeof document.hidden !== "undefined") {
        hidden = "hidden";
        visibilityChange = "visibilitychange";
    } else if (typeof document.msHidden !== "undefined") {
        hidden = "msHidden";
        visibilityChange = "msvisibilitychange";
    } else if (typeof document.webkitHidden !== "undefined") {
        hidden = "webkitHidden";
        visibilityChange = "webkitvisibilitychange";
    }  //else hidden is undefined, and !document[hidden] == true

    var INTERACTION_EVENTS = 'focus resize scroll mousedown mouseup mousemove wheel touchstart touchend touchmove keydown keyup';
    var interactionHappened = false;
    function handleInteraction()
    {
        $(window).off(INTERACTION_EVENTS,handleInteraction);
        interactionHappened = true;
    }

    var visibilityChanged = false;
    function handleVisibilityChange() //not called if there's no Visibility API
    {
        document.removeEventListener(visibilityChange, handleVisibilityChange, false);
        visibilityChanged = true;

        if (!document[hidden]) handleInteraction();
    }

    var intervalsSinceLastInteraction;
    


function RestoreView()
{
    var restoretarget;

    try { restoretarget = localStorage["FLP-last-viewed"] } catch(e) { return }
    if (restoretarget==undefined) return;

    window.location = restoretarget;
}

function RestoreFromURL()
{
    var url = window.location.href;
    var fragindex = url.lastIndexOf("#");
    if (fragindex != -1 && url.substr(fragindex+1) == "restore")
        RestoreView();
    //else
    //    _GAStart();
}
RestoreFromURL();

$(document).ready(function()
{
    var restoretarget;
    try { restoretarget = localStorage["FLP-last-viewed"] } catch(e) { return }
    if (restoretarget != undefined)
    {
       $('div#norestorelinkdiv').remove();
       $('div#restorelinkdiv').css({ 'display':'block'});
       $('a#restorelink').attr('title','View ' + restoretarget);

    }else
    {
       $('div#restorelinkdiv').remove();
       $('div#norestorelinkdiv').css({ 'display':'block'});
    }
});
