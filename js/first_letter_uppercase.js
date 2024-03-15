function capitalize(str){
  
    var parts = str.split(" ")
    var result = parts.map(
       i =>{
        return i[0].toUpperCase() + i.slice(1)
      }
    )
      return result
  
    // for(let i = 0; i<parts.length; i++){
    //   parts[i] = parts[i][0].toUpperCase() + parts[i].slice(1);
    // }
    // return parts.join(" ")
  }
  
  capitalize("this is Antonio practicando")