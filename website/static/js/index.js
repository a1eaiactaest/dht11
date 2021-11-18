var $SCRIPT_ROOT = "";

function write_to_table(values_arr){
  let table = document.getElementById("datatable");
  let row = table.insertRow(1);
  let time_cell = row.insertCell(); time_cell.innerHTML = parse_unix_date(values_arr[0]);
  let id_cell = row.insertCell(); id_cell.innerHTML = values_arr[1];
  let pres_cell = row.insertCell(); pres_cell.innerHTML = values_arr[2] + " hPa";
  let gas_res_cell = row.insertCell(); gas_res_cell.innerHTML = values_arr[3];
  let a_temp_cell = row.insertCell(); a_temp_cell.innerHTML = values_arr[4] + " °C";
  let a_hum_cell = row.insertCell(); a_hum_cell.innerHTML = values_arr[5] + "%";
  let gd_temp_cell = row.insertCell(); gd_temp_cell.innerHTML = values_arr[6] + " °C";
  let gd_hum_cell = row.insertCell(); gd_hum_cell.innerHTML = values_arr[7] + "%";
}

function areEqual(a,b){
  return Array.isArray(a) &&
    Array.isArray(a) && 
    a.length === b.length &&
    a.every((val, index) => val === b[index]);
}

if (location.pathname == '/'){
	var station = 0;
} else {
	var station = document.getElementById('station').innerHTML;
}

function parse_unix_date(unix_seconds){
  var date = new Date(unix_seconds * 1000);
  var year = date.getFullYear();
  var month = date.getMonth();
  var day = date.getDate();
  var hour = date.getHours();
  var minutes = "0" + date.getMinutes();
  var seconds = "0" + date.getSeconds();
  var formatted_time = year + "-" + month + "-" + day + " " + hour + ":" + minutes.substr(-2) + ":" + seconds.substr(-2);
  return formatted_time
}
