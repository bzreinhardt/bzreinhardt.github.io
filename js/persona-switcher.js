var current_persona = "";
var persona_colors = {'Persona_1':'#00ff37',
                      'Persona_2':'#ffe000',
                      'Persona_3':'#0008ff',
                      'Persona_4':'#000000',
                      'Persona_5':'#ff0000',
                      'The_builder':'#00ff37',
                      'The_supporter':'#ffe000',
                      'The_enthusiast':'#0008ff',
                      'The_scholar':'#000000',
                      'The_observer':'#ff0000'};

function clear_persona(){
  var h1 = document.getElementsByTagName("h1");
  for (var i = 0; i < h1.length; i++) {
    h1[i].classList.remove("inactive");
  }
  var h2 = document.getElementsByTagName("h2");
  for (var i = 0; i < h2.length; i++) {
    h2[i].classList.remove("inactive");
  }
  var li = document.getElementsByClassName("toc");
  for (var i = 0; i < li.length; i++){
    li[i].classList.remove("toc_persona");
  }
}

function toggle_persona(persona){
  console.log("toggling persona " + persona);
  var h1 = document.getElementsByTagName("h1");
  for (var i = 0; i < h1.length; i++) {
    var header = h1[i];
    if (header.classList.contains(persona) == false) {
      header.classList.add("inactive");
    } else {
      header.classList.remove("inactive");
    }
  }
  var h2 = document.getElementsByTagName("h2");
  for (var i = 0; i < h2.length; i++) {
    var header = h2[i];
    if (header.classList.contains(persona) == false) {
      header.classList.add("inactive");
    } else {
      header.classList.remove("inactive");
    }
  }
  var li = document.getElementsByClassName("toc");
  for (var i = 0; i < li.length; i++){
    var toc_item = li[i];
    if (toc_item.classList.contains(persona)) {
        toc_item.classList.add("toc_persona");
    } else {
      toc_item.classList.remove("toc_persona");
    }
  }
  var toc_personas = document.getElementsByClassName("toc_persona");
  for (var i=0; i< toc_personas.length; i++){
    toc_personas[i].style.borderLeftColor = persona_colors[persona];
  }
}

$('.persona_button').click(function(){
  var persona = this.innerText.trim().replaceAll("\"","").replaceAll(" ","_");
  if (current_persona == persona) {
    current_persona = "";
    clear_persona();
  } else {
    current_persona = persona;
    toggle_persona(persona);
  }

});

$('.clear_persona').click(function(){
  clear_persona();
});
/*
window.onload = function() {
  var persona_buttons = document.getElementsByClassName("persona_button");
  for (var i=0; i < persona_buttons.length; i++) {
    persona_button = persona_buttons[i];
    persona = persona_button.innerText.trim().replaceAll("\"","").replaceAll(" ","_");
    persona_button.addEventListener("click",toggle_persona(persona));
  }
}
*/
