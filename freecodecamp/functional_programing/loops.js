//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-data-structures/iterate-through-all-an-arrays-items-using-for-loops

function filteredArray(arr, elem) {
  let newArr = [];
  // Only change code below this line
  const present = (x) => x == elem;
  for(let i = 0; i<arr.length; i++){
    if(!arr[i].some(present)){
      newArr.push(arr[i])
    }
  };
  // Only change code above this lin
  return newArr;
}

console.log(filteredArray([[10, 8, 3], [14, 6, 23], [3, 18, 6]], 18));