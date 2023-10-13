/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        console.log("Hello World");
    }
};

console.log("Hola");