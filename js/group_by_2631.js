
//https://leetcode.com/problems/group-by/description/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    var dictionary = {};
    for(i of this){
        if (!(fn(i) in dictionary)){
            dictionary[fn(i)] = [];
        }
        dictionary[fn(i)].push(i);

    }
    return dictionary;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */