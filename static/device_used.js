function getDeviceUsed(devicePercent) {
    console.log("Get Device Used -- LOADED")
      // Load the Visualization API and the piechart package.
      google.charts.load('current', {'packages':['corechart']});
        
      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
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
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Device Type');
        data.addColumn('number', 'Number of people ');
        data.addRows(result);
        //Options of our data
        var options = {
        title: 'Device Used',
        sliceVisibilityThreshold: .05
      };
        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);

      }
}
