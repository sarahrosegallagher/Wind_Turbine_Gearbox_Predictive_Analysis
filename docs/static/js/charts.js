const graphTypes = []

function init() {
  var jsonFilePath = "..\\static\\json\\declare.json"
  
  d3.json(jsonFilePath).then((data) => {
    //console.log(data);
    // Grab a reference to the dropdown select element
    var turbineSelector = d3.select("#selTurbine");
    var metricSelector = d3.select("#selMetric");
    var graphSelector = d3.select("#selGraph");
  
    var turbineNames = Object.keys(data);

    turbineNames.forEach((name) => {
      turbineSelector
        .append("option")
        .text(name)
        .property("value", name);
    });

    var metricNames = Object.keys(data['T01']);

    metricNames.forEach((name) => {
      metricSelector
        .append("option")
        .text(name)
        .property("value", name);
    });

    graphType.forEach((type) => {
      graphSelector
        .append("option")
        .text(type)
        .property("value", type);
    });
  });
};

// Initialize the dashboard
init();

function optionChanged(newSelection) {

  // Fetch new data each time a new option is selected
  buildChart(newSelection);
  
}