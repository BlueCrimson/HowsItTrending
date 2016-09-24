function works() {
	console.log("tweetsOverTime -- LOADED")	
}
function getTweetsOverTime(tweetsOverTime){
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
            data.addColumn('number', 'Day');

      function drawChart() {
      	 // Create our data table out of JSON data loaded from server.
        var json_data = devicePercent;
        
        //Converts json data into an array
        var result = [];
        for(var i in json_data)
        result.push([i, json_data [i]]);

        var options = {
          title: 'Company Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('chart_dive'));

        chart.draw(data, options);
      }
}