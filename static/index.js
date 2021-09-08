var $SCRIPT_ROOT = "";
var acc = 0;


var intervalId = window.setInterval(function(){
  fetch('/info')
    .then(function(response) {
      return response.json();
    }).then(function(text) {
      document.getElementById("humidity").innerHTML = text.humidity;
      document.getElementById("temp").innerHTML = text.temp;
      document.getElementById("heat_index").innerHTML = text.hic;
    });
    acc += 1;
    document.getElementById("acc").innerHTML = acc;
}, 2000);
