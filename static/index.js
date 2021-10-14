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

var intervalId = window.setInterval(function(){
  fetch_data();
}, 5000);

