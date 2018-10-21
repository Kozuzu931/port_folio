function startPocessing(){
  alert("Hellow");
  var element = document.getElementById("result");
  element.textContent = "<p>JavaScriptで書いた内容です</p><p>文字だけかけます</p>";
  element.innerHTML = "<p>JavaScriptで書いた内容です</p><p>HTMLもかけます</p>";
}

var element = document.getElementById("new-post");
element.innerHTML = element.value;
