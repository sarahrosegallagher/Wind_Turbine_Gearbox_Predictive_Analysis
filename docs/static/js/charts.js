const jsonFilePath = "..\\static\\json\\declare.json"
const graphTypes = ["box", "histogram"]

function init() {

  d3.json(jsonFilePath).then((data) => {
    //console.log(data);
    // Grab a reference to the dropdown select element
    var turbineSelector = d3.select("#selTurbine");
    var metricSelector = d3.select("#selMetric");
    var graphSelector = d3.select("#selGraph");

    const turbineNames = Object.keys(data);
  
    turbineNames.forEach((name) => {
      turbineSelector
        .append("option")
        .text(name)
        .property("value", name);
    });

    const metricNames = Object.keys(data['T01']);
    delete metricNames['turbine_id'];
    delete metricNames['time_stamp'];

    metricNames.forEach((name) => {
      metricSelector
        .append("option")
        .text(name)
        .property("value", name);
    });

    graphTypes.forEach((type) => {
      graphSelector
        .append("option")
        .text(type)
        .property("value", type);
    });

    var initialTurbine = turbineNames[0]; 
    var initialMetric = metricNames[2]; 
    var initialGraph = graphTypes[0]; 

    // Initialize the plot with buildChart
    buildChart(initialTurbine, initialMetric, initialGraph)
  });
};

// Initialize the dashboard
init();

function optionChanged(newSelection) {

  // determine which option changed, and build chart with the new information
  // CODE GOES HERE 

  // Fetch new data each time a new option is selected
  // buildChart(newSelection);
  
};

function buildChart(turbine, metric, graph) {

  let turbine_name = turbine;
  console.log(turbine_name);

  let metric_type = metric; 
  console.log(metric_type);

  let graph_type = graph;
  console.log(graph_type);
  
  d3.json(jsonFilePath).then((data) => {

    var plotData = [{
      x: Object.values(data[turbine_name]['time_stamp']),
      y: Object.values(data[turbine_name][metric_type]),
      type: graph_type
    }]; 

    console.log(plotData[0]['x'])


    var trace1 = {
      y: y0,
      type: 'box'
    };

    var plotLayout = {
      title: graph_type, 
      xaxis: {
        title: 'time_stamp'
      }, 
      yaxis: {
        title: metric_type
      }
    };

    // Use Plotly to plot the chart 
    Plotly.newPlot('plot', plotData, plotLayout);

  });

};