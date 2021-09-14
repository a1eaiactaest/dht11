var $SCRIPT_ROOT = "";

function fetch_data(){
  fetch('/info').then(function(response){
    return response.json();
  }).then(function(text){
    var table = document.getElementById("datatable");
    let row = table.insertRow(1);
    let time_cell = row.insertCell();
    let hum_cell = row.insertCell();
    let temp_cell = row.insertCell();
    let hic_cell = row.insertCell();
    time_cell.innerHTML = text.time;
    hum_cell.innerHTML = text.humidity;
    temp_cell.innerHTML = text.temp;
    hic_cell.innerHTML = text.hic;
  });

}

var intervalId = window.setInterval(function(){
  fetch_data();
}, 5000);
