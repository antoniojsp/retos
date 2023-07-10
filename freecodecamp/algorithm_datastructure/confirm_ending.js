function confirmEnding(str, target) {
  let target_length = target.length
  let str_length = str.length

  // console.log(str.slice(str_length-target_length, ))
  return str.slice(str_length-target_length) == target
    ? true : false;
}