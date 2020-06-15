const x_svg = '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><title></title><line x1="8.33414" y1="8.05078" x2="23.8905" y2="23.6071" stroke="#93999E" stroke-width="2" stroke-linecap="round"></line><line x1="23.8906" y1="8.33365" x2="8.33427" y2="23.89" stroke="#93999E" stroke-width="2" stroke-linecap="round"></line></svg>'
const menu_svg = '<svg width="25" height="23" viewBox="0 0 25 23" fill="none"><title></title><line x1="5.5" y1="1.5" x2="24.5" y2="1.5" stroke="#BBBBBB" stroke-linecap="round"></line><circle cx="1.5" cy="1.5" r="1.5" fill="#BBBBBB"></circle><line x1="5.5" y1="16.5" x2="24.5" y2="16.5" stroke="#BBBBBB" stroke-linecap="round"></line><circle cx="1.5" cy="16.5" r="1.5" fill="#BBBBBB"></circle><line x1="9.5" y1="6.5" x2="24.5" y2="6.5" stroke="#BBBBBB" stroke-linecap="round"></line><circle cx="5.5" cy="6.5" r="1.5" fill="#BBBBBB"></circle><line x1="9.5" y1="21.5" x2="24.5" y2="21.5" stroke="#BBBBBB" stroke-linecap="round"></line><circle cx="5.5" cy="21.5" r="1.5" fill="#BBBBBB"></circle><line x1="9.5" y1="11.5" x2="24.5" y2="11.5" stroke="#BBBBBB" stroke-linecap="round"></line><path d="M7 11.5C7 12.3284 6.32843 13 5.5 13C4.67157 13 4 12.3284 4 11.5C4 10.6716 4.67157 10 5.5 10C6.32843 10 7 10.6716 7 11.5Z" fill="#BBBBBB"></path></svg>'


const toggleVisibility = () => {
  if (document.getElementById("toc").classList.contains('active')){
    document.getElementById("toc").classList.remove('active');
    document.getElementsByClassName("IconButton")[0].innerHTML = menu_svg;
  } else {
    document.getElementById("toc").classList.add('active');
    document.getElementsByClassName("IconButton")[0].innerHTML = x_svg;
  }
}
