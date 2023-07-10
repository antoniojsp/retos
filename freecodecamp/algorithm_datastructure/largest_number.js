// function largest(arr){
//   let largest = Number.NEGATIVE_INFINITY;
//   for(let i of arr){
//     if (i > largest){
//       largest = i;
//     }
//   }
//   return largest;
// }


function largestOfFour(arr) {

  let result = [];
  arr.forEach(x=>{
    result.push(x.reduce((largest, x) =>
      {
        return x > largest?x:largest;
      }
    ));
  });

  return result;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);