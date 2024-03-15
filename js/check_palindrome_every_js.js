function isBigEnough(element, index, array) {
    return element == array[array.length - index - 1];
  }
  var a = "almla"
  a = a.split("")
  a.every(isBigEnough); 
  