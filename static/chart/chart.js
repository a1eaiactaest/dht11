function get_initial_data(){
  // change from 0 to variable later
  dates = []; // can't be dict it treats dicts as async despite disabling it
  temps = []

  $.ajax({
    type: 'GET',
    url: '/init/0',
    async: false,
    success: function(fetched){
      fetched.forEach((element, index) => {
        dates.push(element[0]);
        temps.push(element[3]);
      });
    }
  });
  return [dates, temps];
}

arxiv_data = get_initial_data();
n = arxiv_data[0].length;
for (let i=0; i<n; i++){
  console.log([arxiv_data[0][i], arxiv_data[1][i]]);
  //console.log(arxiv_data[1][i]);
}

// dates -> x axis
const labels = arxiv_data[0]; 

const data = {
  labels: labels,
  datasets: [{
    label: 'Temperature over time',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    // temperatures -> y axis
    data: arxiv_data[1]
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
