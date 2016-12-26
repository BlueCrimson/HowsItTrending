    // Load bar chart
    google.charts.load('current', {'packages':['bar']});

    // Set callback so it runs after Google Charts loads
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      var tweetData = new google.visualization.DataTable();
      // Set up the X axis
      tweetData.addColumn('timeofday', 'Time');

      // Set up the Y axis
      tweetData.addColumn('number', 'Number of Tweets');

      // Insert data entries
      tweetData.addRows([
        [[8, 30, 45], 5],
        [[9, 0, 0], 10],
        [[10, 0, 0, 0], 12],
        [[10, 45, 0, 0], 13],
        [[11, 0, 0, 0], 15],
        [[12, 15, 45, 0], 20],
        [[13, 0, 0, 0], 22],
        [[14, 30, 0, 0], 25],
        [[15, 12, 0, 0], 30],
        [[16, 45, 0], 32],
        [[16, 59, 0], 42]
      ]);

      // Options for the bar chart
      var tweetOptions = google.charts.Bar.convertOptions({
        title: 'Tweets Through the day',
        height: 300
      });

      // Initialize the chart
      var tweetChart = new google.charts.Bar(document.getElementById('tweetsOverTime'));

      // Draw with our options
      tweetChart.draw(tweetData, tweetOptions);
    }