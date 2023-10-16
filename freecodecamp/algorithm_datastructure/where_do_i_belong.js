//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/where-do-i-belong


function getIndexToIns(arr, num) {
  arr.sort((a,b)=>a-b)
  let i = 0;
  while (i < arr.length){
    if (arr[i]>=num){
      break;
    };
    i++;
  };
  return i;
};

// getIndexToIns([40, 60], 50);
console.log(getIndexToIns([5, 3, 20, 3], 5) )