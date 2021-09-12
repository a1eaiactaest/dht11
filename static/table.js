/*
function fetch_data(){
  fetch('/data').then(function(response) {
    response.text().then(function(text) {
      return text;
    });
  });
}
*/
var json_data, ret;
const fetch_data = async () => {
  const response = await fetch('/data');
  const json = await response.text();
  return json;
  //console.log(json_data);
}

var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};
  

//https://stackoverflow.com/questions/5180382/convert-json-data-to-a-html-table
function addheaders(list, selector){
  var set = [];
  var headerTr$ = $('<tr/>');

  for (var i=0; i<list.length; i++){
    var rowhash = list[i];
    for (var key in rowhash){
      if ($.inArray(key, set) == -1){
        set.push(key);
        headerTr$.append($('<th/>').html(key));
      }
    }
  }
  $(selector).append(headerTr$);
  return set;

}
function build(selector){
  var json_data = fetch_data();
  console.log(json_data);
  var columns = addheaders(json_data,selector);

  for (var i=0; i < json_data.length; i++){
    var row$ = $('<tr/>');
    for (var coli = 0; coli < columns.length; coli++){
      var cellval = json_data[i][columns[coli]];
      if (cellval = null) cellval = "";
      row$.append($('<td/>').html(cellval));
    }
    $(selector).append(row$);
  }
}

function test(){
  var test = fetch_data();
  console.log(test);
}
