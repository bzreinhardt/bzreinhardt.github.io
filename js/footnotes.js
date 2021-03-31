(function($) {
    "use strict";
    $(document).ready(function() {
        Footnotes.setup();
        var modulefront = $('#main'), overlayMenu = $('#overlay-menu'), navbar = $('#nav-wrapper'), modules = $('.module-front, .module, .module-small'), windowWidth = Math.max($(window).width(), window.innerWidth), navbatTrans, mobileTest;
        var $window = $(window)
          , $html = $('.master');
        function resize() {
            if ($window.width() < 481) {
                return $html.addClass('scrollingnav');
            }
            $html.removeClass('scrollingnav');
        }
        $window.resize(resize).trigger('resize');
        var lastScroll = 0;
        $(window).scroll(function() {
            var nowScroll = $(this).scrollTop();
            if (nowScroll > lastScroll && nowScroll > 300) {
                $('.scrollingnav').fadeOut(600);
            } else {
                $('.scrollingnav').fadeIn(300);
            }
            lastScroll = nowScroll;
        });
        $('.toggle-menu').on('click', function() {
            showMenu();
            $('body').addClass('aux-navigation-active');
            return false;
        });
        $('#overlay-menu-hide').on('click', function() {
            hideMenu();
            $('body').removeClass('aux-navigation-active');
            return false;
        });
        $('.overlay-menu-inner').on('click', function(e) {
            var className = $(e.target).attr('class');
            console.log(className);
            if (!$(e.target).hasClass('link')) {
                hideMenu();
                $('body').removeClass('aux-navigation-active');
                return false;
            }
        });
        $(window).keydown(function(e) {
            if (overlayMenu.hasClass('active')) {
                if (e.which === 27) {
                    hideMenu();
                }
            }
        });
        function showMenu() {
            navbar.animate({
                'opacity': 0,
                'top': -80
            }, {
                duration: 150,
                easing: 'easeInOutQuart'
            });
            overlayMenu.addClass('active');
        }
        function hideMenu() {
            navbar.animate({
                'opacity': 1,
                'top': 0
            }, {
                duration: 150,
                easing: 'easeInOutQuart'
            });
            overlayMenu.removeClass('active');
        }
    });
    $('#overflow-nav > li.slidedown > a').on('click', function() {
        if ($(this).attr('class') != 'active') {
            $('#overflow-nav li ul').slideUp({
                duration: 300,
                easing: 'easeInOutQuart'
            });
            $('#overflow-nav li a').removeClass('active');
            $(this).next().slideToggle({
                duration: 300,
                easing: 'easeInOutQuart'
            }).addClass('open');
            $(this).addClass('active');
        } else {
            $('#overflow-nav li ul').slideUp({
                duration: 300,
                easing: 'easeInOutQuart'
            }).removeClass('open');
            $(this).removeClass('active');
        }
        return false;
    });
    var Footnotes = {
        footnotetimeout: false,
        setup: function() {
            var footnotelinks = $("a[rel='footnote-back']")
            var footnotereflinks = $("a[rel='footnote']")
            $("a[rel='footnote']").on('click', Footnotes.footnotescroll);
            $("a[rel='footnote-back']").on('click', Footnotes.footnotescroll);
            footnotereflinks.unbind('mouseover', Footnotes.footnoteover);
            footnotereflinks.unbind('mouseout', Footnotes.footnoteoout);
            footnotereflinks.bind('mouseover', Footnotes.footnoteover);
            footnotereflinks.bind('mouseout', Footnotes.footnoteoout);
        },
        footnoteover: function() {
            clearTimeout(Footnotes.footnotetimeout);
            $('#footnotediv').stop();
            $('#footnotediv').remove();
            var id = $(this).attr('href').substr(1);
            var position = $(this).offset();
            var div = $(document.createElement('div'));
            div.attr('id', 'footnotediv');
            div.bind('mouseover', Footnotes.divover);
            div.bind('mouseout', Footnotes.footnoteoout);
            var el = document.getElementById(id);
            div.html($(el).html());
            $(document.body).append(div);
            var left = position.left;
            if (left + (div.width() + 20) > $(window).width())
                left = $(window).width() - (div.width() + 20);
            var top = position.top + 20;
            if (top + div.height() > $(window).height() + $(window).scrollTop())
                top = position.top - div.height() - 15;
            div.css({
                left: left,
                top: top
            });
        },
        footnoteoout: function() {
            Footnotes.footnotetimeout = setTimeout(function() {
                $('#footnotediv').animate({
                    opacity: 0
                }, 600, function() {
                    $('#footnotediv').remove();
                });
            }, 100);
        },
        divover: function() {
            clearTimeout(Footnotes.footnotetimeout);
            $('#footnotediv').stop();
            $('#footnotediv').css({
                opacity: 0.9
            });
        },
        footnotescroll: function(e) {
            var t, a, n, r, o, i;
            if (location.pathname.replace(/^\//, "") === this.pathname.replace(/^\//, "") || location.hostname === this.hostname) {
                if (e.preventDefault(),
                o = $("nav.navbar").height() + 32,
                $(this).hasClass("footnote-backref"))
                    return i = "footnote-highlight",
                    n = $(this),
                    t = $('[id="' + n.attr("href").slice(1) + '"]'),
                    a = t.closest("p, ul, ol, sup"),
                    a.addClass(i),
                    a.one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function() {
                        return console.log("hello"),
                        a.removeClass(i)
                    }),
                    $("html,body").animate({
                        scrollTop: a.offset().top - o
                    }, 500),
                    !1;
                if ($(this).hasClass("footnote-ref")) {
                    if (r = this.hash.slice(1),
                    n = $('[id="' + r + '"]'),
                    n.length)
                        return $("html,body").animate({
                            scrollTop: n.offset().top - o
                        }, 500),
                        !1
                } else if (n = $(this.hash),
                n = n.length ? n : $('[name="' + this.hash.slice(1)(NaN)),
                n.length)
                    return $("html,body").animate({
                        scrollTop: n.offset().top - o
                    }, 500),
                    !1
            }
        }
    }
    $(document).ready(function() {
        $('a[href^="#"]:not(a[rel="footnote"]):not(a[rev="footnote"]):not(a[id="backtotop"])').on('click', function(e) {
            e.preventDefault();
            var target = this.hash;
            var $target = $(target);
            $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, 500, 'swing');
        });
        $('a[id="backtotop"]').on('click', function(e) {
            e.preventDefault();
            $('html, body').stop().animate({
                scrollTop: 0
            }, 400, 'swing');
        });
    });
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scroll-up').fadeIn();
        } else {
            $('.scroll-up').fadeOut();
        }
    });
    $('a[href="#main]').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 'slow');
        return false;
    });
    $('.footnote-backref').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 50
            }, 500);
        }
    });
    /*
    $(function() {
        $('#nav-wrapper').height($("#nav").height());
        $('#nav').affix({
            offset: {
                top: $('#nav').offset().top
            }
        });
    });
    */
    /*
    $(document).ready(function() {
        var i = 0;
        document.querySelectorAll('.codehilite > pre').forEach(function(codeBlock, i) {
            var button = document.createElement('button');
            button.className = 'copy-code-button';
            button.type = 'button';
            button.innerText = '';
            button.setAttribute('title', 'Copy content');
            button.innerHTML = '<i class="icon-copy"></i>';
            button.setAttribute('data-clipboard-target', '#code-' + parseInt(i));
            var pre = codeBlock;
            codeBlock.setAttribute('id', 'code-' + parseInt(i));
            pre.insertBefore(button, pre.firstChild);
            i++;
        });
        var clipboard = new ClipboardJS(".copy-code-button");
    });

    $(document).ready(function() {
        $(".slider").slick({
            infinite: true,
            dots: true,
            adaptiveHeight: true,
            arrows: true,
            lazyLoad: 'ondemand',
            responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    infinite: true
                }
            }, {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    dots: true
                }
            }, {
                breakpoint: 300,
                settings: "unslick"
            }]
        });
    });
    */
}
)(jQuery);
