//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/truncate-a-string

function truncateString(str, num) {
  if(str.length <= num){
    return str;
  }
  let ending = "...";
  let starting = str.slice(0,num);

  return starting + ending;
}

truncateString("A-tisket a-tasket A green and yellow basket", 8);