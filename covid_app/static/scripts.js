const countries = top10.map(i => i.country);
const cases = top10.map(i => i.cases);
const deaths = top10.map(i => i.deaths);

Plotly.newPlot('plotlyChart', [
  { x: countries, y: cases, name: 'Cases', type: 'bar' },
  { x: countries, y: deaths, name: 'Deaths', type: 'bar' }
], { barmode: 'group', title: 'Cases vs Deaths' });

fetch("/api/trend/")
  .then(res => res.json())
  .then(json => {
    new Chart(document.getElementById("trendChart"), {
      type: 'line',
      data: {
        labels: json.labels,
        datasets: [{
          label: 'Daily Cases',
          data: json.data,
          borderColor: '#00f',
          fill: false
        }]
      }
    });
  });
