var $SCRIPT_ROOT = "";

function fetch_data(station){
  let url = $SCRIPT_ROOT + '/info/' + station;
  $.post(url, function(response){
    let data = response[0];
    write_to_table(data);
  });
}

function write_to_table(values_arr){
    let table = document.getElementById("datatable");
    let row = table.insertRow(1);
    let time_cell = row.insertCell(); time_cell.innerHTML = values_arr[0];
    let id_cell = row.insertCell(); id_cell.innerHTML = values_arr[1];
    let pres_cell = row.insertCell(); pres_cell.innerHTML = values_arr[2] + " hPa";
    let gas_res_cell = row.insertCell(); gas_res_cell.innerHTML = values_arr[3];
    let a_temp_cell = row.insertCell(); a_temp_cell.innerHTML = values_arr[4] + " °C";
    let a_hum_cell = row.insertCell(); a_hum_cell.innerHTML = values_arr[5] + "%";
    let gd_temp_cell = row.insertCell(); gd_temp_cell.innerHTML = values_arr[6] + " °C";
    let gd_hum_cell = row.insertCell(); gd_hum_cell.innerHTML = values_arr[7] + "%";
}



if (location.pathname == '/'){
	var station = 0;
} else {
	var station = document.getElementById('station').innerHTML;
}
console.log(station);

// init archive data
$.get("/init/" + station, function(data){
	for (const value_set of data){
		write_to_table(value_set);
	}
});

var intervalId = window.setInterval(function(){
	fetch_data(station);
}, 10000);


