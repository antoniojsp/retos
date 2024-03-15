function anagram(str1, str2){
    // var test = (x) => {
    //   var code = x.charCodeAt(0);
    //   return 97 <= code && code <= 122
    // }
    // var string1 = str1.toLowerCase().split("").sort().filter(test);
    // var string2 = str2.toLowerCase().split("").sort().filter(test);
    // return string1.join("") == string2.join("")
    var string1 = str1.replace(/\W/g,  "").toLowerCase().split("").sort();
    var string2 = str2.replace(/\W/g,  "").toLowerCase().split("").sort();
    
    return string1.join("") == string2.join("")
  }
  
  

function anagram(s1,s2){
  
    var count = (s) => {
      const seen = {}
      for(i of s){
        seen[i] = ++seen[i] || 1
      }
      return seen
    }
    s1 = count(s1.toLowerCase().replace(/\W/g, ""));
    s2 = count(s2.toLowerCase().replace(/\W/g, ""));
    
    for(i of Object.keys(s1)){
      if(s1[i] == s2[i]){
        delete s1[i]
      }else{
        return false;
      }
    }
    console.log(s1)
    
    return Object.keys(s1).length == 0
    
    
  }

console.log(anagram("RAIL SAFETY!", 'fairy tales'))
