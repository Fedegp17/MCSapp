
// setup

    const data = {
      labels: ['Mon', 'Tue'],
      datasets: [{
        label: 'Weekly Sales',
        data: [89, 20],
        backgroundColor: [
          'rgba(0, 63, 147, 0.8)',
          'rgba(0, 0, 0, 0.2)'
        ],
        borderColor: [
          'rgba(0, 63, 147, 0.8)',
          'rgba(0, 0, 0, 0.2)'
        ],
        borderWidth: 1,
        cutout: '80%',
        circumference: 180,
        rotation: 270,
      }]
    };

    // gauge ChartText config
    const gaugeChartText = {
        id: 'gaugeChartText2',
        afterDatasetsDraw(chart, agrs, pluginOptions) {
            const { ctx, data, chartArea: {top, bottom, left, right, width, height}, scales: {r} } = chart;

            ctx.save();
            const xCoor = chart.getDatasetMeta(0).data[0].x;
            const yCoor = chart.getDatasetMeta(0).data[0].y;
            const score = data.datasets[0].data[0];
            let rating;

            if(score ==0 ) { rating = 'Asistolia'; }
            if(score >= 1 && score <= 29) { rating = 'Bradicardia'; }
            if(score >= 30 && score <= 59) { rating = 'Bradicardia'; }
            if(score >= 60 && score <= 100) { rating = 'Ritmo sinusal'; }
            if(score >= 101 && score <= 149) { rating = 'Taquicardia'; }
            if(score >= 150) { rating = 'Taquicardia-Peligro'; }


            //Function created for writing the labels of the chart to save lines of code
            function textLabel(text, x, y, fontSize, textBaseLine, textAlign){
                ctx.font = `${fontSize}px sans-serif`;
                ctx.fillStyle = '#666';
                ctx.textBaseLine = textBaseLine;
                ctx.textAlign = textAlign;
                ctx.fillText(text, x, y);
            }

            //Adding the limit values of the chart (0 & 220 i.e.)
            textLabel('0', left, yCoor + 20, 20, 'top', 'left');
            textLabel('220', right, yCoor + 20, 20, 'top', 'right');

            //Adding the value registered by the chart
            textLabel(score, xCoor, yCoor, 25, 'bottom', 'center');

            //Adding the rating or category depending on the registered value
            textLabel(rating, xCoor, yCoor - 25, 15, 'bottom', 'center');

        }
    }

    // config
    const config = {
      type: 'doughnut',
      data,
      options: {
        aspectRatio: 1,
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            }
        }
      },
      plugins: [gaugeChartText]
    };

    // render init block
    const myChart = new Chart(
      document.getElementById('SPO2Chart'),
      config
    );

    // Instantly assign Chart.js version
    const chartVersion = document.getElementById('chartVersion');
    chartVersion.innerText = Chart.version;