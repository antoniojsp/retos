//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/finders-keepers

function findElement(arr, func) {

  for(let i of arr){
    if(func(i)){
      return i;
    }
  }

  return undefined;
}