function steps(num){

    for (let i = 1;i<num+1; i++){
      var temp = ""
       for (let j = 1;j<i+1; j++){
           temp += "#"
        }
        console.log(temp)
    }
  }
  
  steps(3)