var $SCRIPT_ROOT = "";

function fetch_data(station){
  let url = $SCRIPT_ROOT + '/info/' + station;
  $.get(url, function(response){
    let data = response[0];
    write_to_table(data);
  });
}


