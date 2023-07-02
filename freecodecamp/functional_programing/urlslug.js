//https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/functional-programming/apply-functional-programming-to-convert-strings-to-url-slugs

// Only change code below this line
function urlSlug(title){

    let slug = title.toLowerCase().trim().split(/\W/).filter(
                  (x) => { if(x!=" "){
                        return x
                  }}
                ).join("-");

return slug
};
// Only change code above this line
a = urlSlug(" Winter Is  Coming");
a
