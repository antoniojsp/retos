//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/title-case-a-sentence

function titleCase(str) {

let lista = str.split(" ")
let result = lista.map(x=>{
  return x[0].toUpperCase() + x.slice(1).toLowerCase()
})
  return result.join(" ");
}

titleCase("I'm a little tea pot");