
arxiv_data = get_initial_data();
/*
n = arxiv_data[0].length;
for (let i=0; i<n; i++){
  console.log([arxiv_data[0][i], arxiv_data[1][i]]);
  //console.log(arxiv_data[1][i]);
}
*/

// dates -> x axis
const labels = arxiv_data[0]; 

const data = {
  labels: labels,
  datasets: [{
    label: 'Temperature over time',
    backgroundColor: 'rgb(60, 200, 50)',
    borderColor: 'rgb(60, 200, 50)',
    // temperatures -> y axis
    data: arxiv_data[1],
    tension: 0.3
  }]
};

const config = {
  type: 'line',
  data: data,
  options: {}
};

var myChart = new Chart(
  document.getElementById('chart').getContext('2d'),
  config
);

function get_initial_data(){
  // change from 0 to variable later
  ret = [[],[]]

  $.ajax({
    type: 'GET',
    url: '/init/0',
    async: false,
    success: function(fetched){
      fetched.forEach((element, index) => {
        ret[0].push(element[0]);
        ret[1].push(element[4]);
      });
    }
  });
  return ret;
}

function fetch_data(station){
  let url = '/info/' + station;
  $.post(url, function(response){
    let data = response[0];
    console.log(data);
    add_data(myChart, data[0], data[4]);
  });
}

function add_data(chart, label, data){
  chart.data.labels.push(label);
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
  });
  chart.update();
}

var intervalId = window.setInterval(function(){
  fetch_data(0);
}, 10000);

