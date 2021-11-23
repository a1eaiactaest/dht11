import {parse_unix_time} from './utils.js';
// make it global variable
if (location.pathname == '/'){
  var station = 0;
} else {
  var station = document.getElementById('station').innerHTML;
}

var NUM_POINTS;
var station = document.getElementById('station').innerHTML;
var arxiv_data = get_initial_data(station);

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
    normalized: true,
    animation: false,
    plugins: {
      decimation: decimation,
    },
    spanGaps: true,
    scales: {
      y: {
        grace: '5'
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

function get_initial_data(station){
  // change from 0 to variable later
  var ret = [[],[]]

  $.ajax({
    type: 'GET',
    url: '/init/'+ station + '/' + '100',
    async: false,
    success: function(fetched){
      fetched.forEach((element, index) => {
        ret[0].push(parse_unix_time(element[0]));
        ret[1].push(element[4]);
      });
    }
  });
  NUM_POINTS = ret.length;
  return ret;
}

function add_data(chart, label, data){
  chart.data.labels.push(label);
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
  });
  chart.update()
}

export {myChart, add_data};
