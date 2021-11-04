// using this later in chart config
var min_arxiv = 0;
var max_arxiv = 0;

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

// make less points on a chart
const decimation = {
  enabled: true,
  algorithm: 'lttb',
};

const actions = [
  {
  name: 'lttb',
  handler(chart) {
    chart.options.plugins.decimation.algorithm = 'lttb',
    chart.options.plugins.decimation.enabled = true,  
    chart.options.plugins.decimation.samples = 50,  
    chart.update()
  }
  }
];

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
  options: {
    plugins: {
      deecimation: decimation,
    },
    spanGaps: true,
    scales: {
      y: {
        max: max_arxiv+5,
        min: min_arxiv-5
      },
      xAxes: {
        ticks: {
          autoSkip: true,
          maxTicksLimit: 10
        }
      }
    }
  }
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
  min_arxiv = Math.min(...ret[1]); 
  max_arxiv = Math.max(...ret[1]);
  return ret;
}

/*
function fetch_data(station){
  let url = '/info/' + station;
  $.post(url, function(response){
    let data = response[0];
    add_data(myChart, data[0], data[4]);
  });
}
*/

function add_data(chart, label, data){
  chart.data.labels.push(label);
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
  });

  console.log(data);
  if (data > max_arxiv){
    max_arxiv = data;
  }

  if (data < min_arxiv){
    min_arxiv = data;
  }
  updateScale(myChart, min_arxiv, max_arxiv);
}

function updateScale(chart, min, max){
  chart.options.scales.y = {
    max: max+5,
    min: min-5
  };
  chart.update()
}

/*
var intervalId = window.setInterval(function(){
  fetch_data(0);
}, 10000);
*/
