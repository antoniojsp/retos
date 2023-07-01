function countdown(n){

  if (n <= 0){
    return []
  }
  return [...[n],...countdown(n-1)]
}


countdown(5);