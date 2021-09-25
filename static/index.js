var $SCRIPT_ROOT = "";
var acc = 0;

/*
var intervalId = window.setInterval(function(){
  fetch('/info')
    .then(function(response) {
      return response.json();
    }).then(function(text) {
      console.log(Array.from(text));
      document.getElementById("time").innerHTML = text.time;
      document.getElementById("humidity").innerHTML = text.humidity;
      document.getElementById("temp").innerHTML = text.temp;
      document.getElementById("heat_index").innerHTML = text.hic;
    });
    acc += 1;
    document.getElementById("acc").innerHTML = acc;
}, 5000); // it'd be the best if this value is the same or bigger than the one in dht11.ino.
*/

var $SCRIPT_ROOT = "";

function fetch_data(){
  fetch('/info').then(function(response){
    return response.json();
  }).then(function(text){
    let values = text[0]
    console.log(values);
    let table = document.getElementById("datatable");
    let row = table.insertRow(1);
    let time_cell = row.insertCell(); time_cell.innerHTML = values[0];
    let id_cell = row.insertCell(); id_cell.innerHTML = values[1];
    let pres_cell = row.insertCell(); pres_cell.innerHTML = values[2];
    let gas_res_cell = row.insertCell(); gas_res_cell.innerHTML = values[3];
    let a_temp_cell = row.insertCell(); a_temp_cell.innerHTML = values[4];
    let a_hum_cell = row.insertCell(); a_hum_cell.innerHTML = values[5];
    let gd_temp_cell = row.insertCell(); gd_temp_cell.innerHTML = values[6];
    let gd_hum_cell = row.insertCell(); gd_hum_cell.innerHTML = values[7];
    let gps_lat_cell = row.insertCell(); gps_lat_cell.innerHTML = values[8];
    let gps_lon_cell = row.insertCell(); gps_lon_cell.innerHTML = values[9];
    let gps_angle_cell = row.insertCell(); gps_angle_cell.innerHTML = values[10];
    let gps_speed_cell = row.insertCell(); gps_speed_cell.innerHTML = values[11];
  });

}

var intervalId = window.setInterval(function(){
  fetch_data();
}, 3000);

