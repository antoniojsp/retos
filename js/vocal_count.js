// function count_vocals(str){
  
//   var pattern = /[aeiou]/g 
  
//   return str.match(pattern).length;
  
// }

function count_vocals(str){
    var count = 0;
    pattern = new Set("aeiou".split(""));
    for (i of str){
      if (pattern.has(i)){
        count+=1;
      }
    };
    return count;
  }
  
  count_vocals("antonio")
  
  