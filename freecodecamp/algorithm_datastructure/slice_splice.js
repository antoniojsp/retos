//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/slice-and-splice


function frankenSplice(arr1, arr2, n) {
  let first = arr2.slice(0, n);
  let end = arr2.slice(n)

  first.push(...arr1)
  first.push(...end)

  return first
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);