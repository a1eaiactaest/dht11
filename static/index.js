var $SCRIPT_ROOT = "";
var acc = 0;


var intervalId = window.setInterval(function(){
  fetch('/info')
    .then(function(response) {
      return response.json();
    }).then(function(text) {
      console.log(text.humidity);
      document.getElementById("humidity").innerHTML = text.humidity;
      console.log(text.temp);
      document.getElementById("temp").innerHTML = text.temp;
      console.log(text.hic);
      document.getElementById("heat_index").innerHTML = text.hic;
    });
    acc += 1;
    document.getElementById("acc").innerHTML = acc;
}, 2000);
