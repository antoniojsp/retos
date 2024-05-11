var examples = 120;

var result = 0
while (examples > 0){
  let digit = examples%10;
  result = result * 10 + digit
  examples = Math.floor(examples/10);
}

console.log(result)


// 120%10 = 0
// 120/10 = 12

// 12%10  = 2
// 12/10 = 1.2 or 1
// 1%10
// 1