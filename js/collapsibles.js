// This code will create clickable collapsables for any section with the class 'collapsibe'
// That collapses anything labelled "content"
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].classList.toggle("active");
  content = coll[i].nextElementSibling;
  content.style.maxHeight = content.scrollHeight + "px";
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight != "0px"){
      content.style.maxHeight = "0px";
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

/*
Associated CSS
<style>
.collapsible {
  background-color: white;
  color: black;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.collapsible:after {
  content: '\002B';
  color: white;
  font-weight: bold;
  float: right;
  margin-left: 5px;
}

.active:after {
  content: "\2212";
}

.content {
  padding: 0 18px;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}
</style>
*/
