var id;
var position = 0;

function startAnimetion(){
  id = setInterval(tick, 1);
}

function tick(){
  var element = document.getElementById("object");
  if (position == 350){
    clearInterval(id);
  }
  else {
    position++;
    element.style.top = position/2 + "px";
    element.style.left = position/2 + "px";
  }
}
