/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */


function counter(str){
    var arr = new Array(26).fill(0);
    for (let i of str){
      arr[i.charCodeAt(0)-97]++;
    }
    return arr;
  }
  
  var canConstruct = function(ransomNote, magazine) {
    if (ransomNote.length > magazine.length) return false;
    var ramson_freq = counter(ransomNote);
    var zine_freq  = counter(magazine);
  
    for(let i = 0; i<ramson_freq.length; i++){
      if(ramson_freq[i]>zine_freq[i]){
         return false;
      }
    }
      return true;
  };    