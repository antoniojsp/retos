function repeatStringNumTimes(str, num) {
  if(num < 0){
    return ""
  }

  let result = "";

  let i = 0;
  while (i<num){
    result +=str;
    ++i;
  }

  return result;
}

repeatStringNumTimes("abc", 3);