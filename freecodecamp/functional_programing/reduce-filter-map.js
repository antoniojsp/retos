//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/functional-programming/use-higher-order-functions-map-filter-or-reduce-to-solve-a-complex-problem

const squareList = arr => {
  // Only change code below this line
  let result = arr.filter(x => x > 0 && x%1==0).map(
    x =>x**2
  );

  return result;
  // Only change code above this line
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);