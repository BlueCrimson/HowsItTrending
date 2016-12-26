function getDeviceUsed(devicePercent) {
    console.log("Get Device Used -- LOADED")
      // Load the Visualization API and the piechart package.
      google.charts.load('current', {'packages':['corechart','bar']});
        
      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawPieChart);

      function drawPieChart() {
        var jsonData = $.ajax({
            url: "getData.php",
            dataType: "json",
            async: false
            }).responseText;
            
        // Create our data table out of JSON data loaded from server.
        var json_data = devicePercent;
        
        //Converts json data into an array
        var result = [];
        for(var i in json_data)
            result.push([i, json_data [i]]);

        //Creating our data obj that will be presented as a pie chart
        var deviceData = new google.visualization.DataTable();
        deviceData.addColumn('string', 'Device Type');
        deviceData.addColumn('number', 'Number of people ');
        deviceData.addRows(result);

        //Options of our data
        var deviceOptions = {
        title: 'Device Used',
        // Min % for slice (.05 = 5%), otherwise its casted to other
        sliceVisibilityThreshold: .05
      };
        // Instantiate and draw our chart, passing in some options.
        var deviceChart = new google.visualization.PieChart(document.getElementById('devicePieChart'));
        deviceChart.draw(deviceData, deviceOptions);
        //TEST TEST TEST
        
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
}
