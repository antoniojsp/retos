//https://leetcode.com/problems/add-binary/description/
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */

function fill_zeros(arr, total){
  var fills = new Array(total - arr.length).fill("0")
  return fills.concat(arr)
}

var addBinary = function(a, b) {

  var first = [...a]
  var second = [...b]
  var result = []
  var carry = 0;

  if (first.length > second.length){
     second = fill_zeros(second, first.length)
  }else if (first.length < second.length){
     first = fill_zeros(first, second.length)
  }
  first = first.reverse();
  second = second.reverse()

  for(let i = 0;i<first.length;i++){
    if(first[i] == 1 && second[i] == 1){
      result.push(0+carry);
      carry=1;
    }else if(first[i] == 0 && second[i] == 0){
      result.push(0+carry);
      carry = 0
    }else{
      if (carry==1){
          result.push(0);
        carry =1
      }else{
        result.push(1)
        carry = 0
      }
    }
  };

  if (carry==1){
    result.push(1)
  }

  return result.reverse().join("")
};

