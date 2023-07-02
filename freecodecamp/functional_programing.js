Array.prototype.myFilter = function(callback) {
  const newArray = [];
  // Only change code below this line
  this.forEach((elem, index, arr) => {
    if(callback(elem, index, arr)){
      newArray.push(elem);
    }
  });
  // Only change code above this line
  return newArray;
};

Array.prototype.myMap = function(callback) {
  const newArray = [];
  // Only change code below this line
  for (let i = 0; i < this.length; i++) {
    newArray.push(callback(this[i], i, this));
  }
  // Only change code above this line
  return newArray;
};