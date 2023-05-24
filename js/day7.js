/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {

        if (functions.length === 0){
            return x
        }
        var result = x;
        for (let i = functions.length - 1 ; i >= 0 ; i--){
           var current = functions[i];
            result = current(result)

        };

        return result
    };
    
};
