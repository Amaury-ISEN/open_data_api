Highcharts.chart('chart', {
    chart: {
      type: 'bar'
    },
    title: {
      text: donnees[0]
    },
    subtitle: {
      text: 'Source: <a href="https://www.insee.fr/fr/statistiques?debut=0&theme=0">insee.fr</a>'
    },
    xAxis: {
      categories: ['Retour au domicile', 'Décès'],
      title: {
        text: null
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: 'Population',
        align: 'high'
      },
      labels: {
        overflow: 'justify'
      }
    },
    tooltip: {
      valueSuffix: ' personnes'
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
      x: -20,
      y: 180,
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
      data: [donnees[1]]
    }, {
      name: 'Gaz',
      data: [donnees[2]]
    }, {
      name: 'Electricité',
      data: [donnees[3]]
    }]
  });