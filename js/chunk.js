function chunk(arr, step){
  
    var list = []
    for(let i = 0; i < arr.length; i = i + step){
      list.push(arr.slice(i,i+step))
    }
  return list
}


chunk([1,2,3,4,5], 3)