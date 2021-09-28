var $SCRIPT_ROOT = "";

// init archive data
$.get("/init", function(data){
  for (const value_set of data){
    write_to_table(value_set);
  }
});

function fetch_data(){
  $.get('/info', function(response){
    let data = response[0];
    write_to_table(data);
  })
}

function write_to_table(values_arr){
    let table = document.getElementById("datatable");
    let row = table.insertRow(1);
    let time_cell = row.insertCell(); time_cell.innerHTML = values_arr[0];
    let id_cell = row.insertCell(); id_cell.innerHTML = values_arr[1];
    let pres_cell = row.insertCell(); pres_cell.innerHTML = values_arr[2];
    let gas_res_cell = row.insertCell(); gas_res_cell.innerHTML = values_arr[3];
    let a_temp_cell = row.insertCell(); a_temp_cell.innerHTML = values_arr[4];
    let a_hum_cell = row.insertCell(); a_hum_cell.innerHTML = values_arr[5];
    let gd_temp_cell = row.insertCell(); gd_temp_cell.innerHTML = values_arr[6];
    let gd_hum_cell = row.insertCell(); gd_hum_cell.innerHTML = values_arr[7];
    let gps_lat_cell = row.insertCell(); gps_lat_cell.innerHTML = values_arr[8];
    let gps_lon_cell = row.insertCell(); gps_lon_cell.innerHTML = values_arr[9];
    let gps_angle_cell = row.insertCell(); gps_angle_cell.innerHTML = values_arr[10];
    let gps_speed_cell = row.insertCell(); gps_speed_cell.innerHTML = values_arr[11];
}

var intervalId = window.setInterval(function(){
  fetch_data();
}, 900000); 

