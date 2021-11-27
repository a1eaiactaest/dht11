import {myChart, add_data} from './chart.js';
import {write_to_table} from './table.js';
import {are_equal, parse_unix_time} from './utils.js';

var $SCRIPT_ROOT = "";
export var recent = [];
export function fetch_data(station){
  let url = $SCRIPT_ROOT + '/info/' + station;
  $.post(url, function(response){
    let data = Object.values(response[0]);
    if (!are_equal(data, recent)){
      write_to_table(data);
      add_data(myChart, parse_unix_time(data[0]), data[4]);
    } else {
      console.log('element has been already requested: ' + data);
    }
    recent = data;
  });
}

export function init_data(station){
 var select = document.getElementById("amount");
 var rowAmount = select.options[select.selectedIndex].value;
 $.get('/init/' + station + '/' + rowAmount, function(data){
   for (const value_set of data){
     write_to_table(value_set);
     recent = value_set;
   }
 });
}
