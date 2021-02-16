Highcharts.chart('chart', {
    chart: {
      type: 'bar',
      height: 550,
      width: 1000
    },
    title: {
      text: donnees[0]
    },
    subtitle: {
      text: 'Source: <a href="https://www.insee.fr/fr/statistiques?debut=0&theme=0">insee.fr</a>'
    },
    xAxis: {
      categories: donnees[4],
      title: {
        text: null
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: 'Consommation (en MWh)',
        align: 'high'
      },
      labels: {
        overflow: 'justify'
      }
    },
    tooltip: {
      valueSuffix: '  MWh'
    },
    plotOptions: {
      bar: {
        dataLabels: {
          enabled: true
        }
      }
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      x: -5,
      y: 410,
      floating: true,
      borderWidth: 1,
      backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
      shadow: true
    },
    credits: {
      enabled: false
    },
    series: [{
      name: 'Toutes filières',
      data: donnees[1]
    }, {
      name: 'Gaz',
      data: donnees[2]
    }, {
      name: 'Electricité',
      data: donnees[3]
    }]
  });