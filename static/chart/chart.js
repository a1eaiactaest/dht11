function get_initial_data(){
  // change from 0 to variable later
  ret = [];
  $.ajax({
    type: 'GET',
    url: '/init/0',
    async: false,
    success: function(fetched){
      ret = fetched
    }
  });
  console.log(ret);
  return ret;
}

val = get_initial_data();
console.log(val);
n = val.length;
for (let i=0; i<n; i++){
  console.log(val[i]);
}

const labels = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
];

const data = {
  labels: labels,
  datasets: [{
    label: 'Temperature over time',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: [0, 10, 5, 2, 20, 30, 45],
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
