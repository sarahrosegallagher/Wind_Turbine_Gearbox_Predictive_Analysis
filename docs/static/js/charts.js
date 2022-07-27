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

    var metricNames = Object.keys(data['T01']);
    metricNames.shift(); 
    metricNames.shift();
    console.log(metricNames);

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
    var initialMetric = metricNames[0]; 
    var initialGraph = graphTypes[0]; 

    // Initialize the plot with buildChart
    buildChart(initialTurbine, initialMetric, initialGraph)
  });
};

// Initialize the dashboard
init();

function optionChanged(newSelection) {

  d3.json(jsonFilePath).then((data) => {

    const turbineNames = Object.keys(data);

    var metricNames = Object.keys(data['T01']);
    delete metricNames['turbine_id'];
    delete metricNames['time_stamp'];

    // determine which option changed, and build chart with the new information
    if (turbineNames.includes(newSelection)) {
      var newTurbine = newSelection;

      var select = document.getElementById('selMetric');
      var currentMetric = select.options[select.selectedIndex].value;

      select = document.getElementById('selGraph');
      var currentGraph = select.options[select.selectedIndex].value;

      buildChart(newTurbine, currentMetric, currentGraph)
    }
    else if (metricNames.includes(newSelection)) {
      var newMetric = newSelection;

      var select = document.getElementById('selTurbine');
      var currentTurbine = select.options[select.selectedIndex].value;

      select = document.getElementById('selGraph');
      var currentGraph = select.options[select.selectedIndex].value;

      buildChart(currentTurbine, newMetric, currentGraph)
    }
    else if (graphTypes.includes(newSelection)) {
      var newGraph = newSelection;

      var select = document.getElementById('selTurbine');
      var currentTurbine = select.options[select.selectedIndex].value;

      select = document.getElementById('selMetric');
      var currentMetric = select.options[select.selectedIndex].value;

      buildChart(currentTurbine, currentMetric, newGraph)
    }

  });
  
};

function buildChart(turbine, metric, graph) {

  let turbine_name = turbine;
  console.log(turbine_name);

  let metric_type = metric; 
  console.log(metric_type);

  let graph_type = graph;
  console.log(graph_type);
  
  d3.json(jsonFilePath).then((data) => {

    
    //var plotData = [{
      //x: Object.values(data[turbine_name]['time_stamp']),
      //y: Object.values(data[turbine_name][metric_type]),
      //type: graph_type
    //}]; 

    //console.log(plotData[0]['x'])
    if (graph_type == "box") {
      var plotData = [{
        y: Object.values(data[turbine_name][metric_type]),
        type: graph_type
      }];
      var plotLayout = {
        title: "Box Plot",
        yaxis: {
          title: metric_type
        }, 
        xaxis: {
          title: turbine_name
        }
      };
    }
    else if (graph_type == "histogram") {
      var plotData = [{
        x: Object.values(data[turbine_name][metric_type]),
        type: graph_type
      }];
      var plotLayout = {
        title: "Histogram",
        yaxis: {
          title: metric_type
        },
        xaxis: {
          title: turbine_name
        }
      };
    };

    // Use Plotly to plot the chart 
    Plotly.newPlot('plot', plotData, plotLayout);

  });

};
