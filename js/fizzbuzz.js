function fizzbuzz(num){
    
    for (let i = 1; i<num+1; i++){
      switch(true){
        case (i%15 == 0):
          console.log("fizzbuzz");
          break;
        case (i%3 == 0):
          console.log("fizz");
          break;
        case (i%5 == 0):
          console.log("buzz");
          break;
        default:
          console.log(i);
  
      }
    }
};

fizzbuzz(115)