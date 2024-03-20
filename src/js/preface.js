var Module = {
  stdout : "",
  resetOut: function() { Module.stdout = ""; },
  print: function(text) { Module.stdout += text; },
};
