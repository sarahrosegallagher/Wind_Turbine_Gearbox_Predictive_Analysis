function init() {
    var selector = d3.select("#selTurbine");
  
    d3.json("samples.json").then((data) => {
      //console.log(data);
      var sampleNames = data.names;
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  })};