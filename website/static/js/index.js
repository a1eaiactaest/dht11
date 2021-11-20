import {fetch_data, init_data} from './requests_handler.js';

if (location.pathname == '/'){
	var station = 0;
} else {
	var station = document.getElementById('station').innerHTML;
}
console.log(station);

if (station != 0){
  console.log(document.getElementById("title").innerHTML);
  document.getElementById("title").innerHTML = "Stacja " + station;
}

function main(station){
  // run on the load of the page
  init_data(station); 
}

window.onload = (event) => {
  main(station);
};

// This is run every 10 seconds
var intervalId = window.setInterval(function(){
  fetch_data(station)
}, 10000);

