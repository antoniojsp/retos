// https://leetcode.com/problems/allow-one-function-call/submissions/?utm_campaign=PostD8&utm_medium=Post&utm_source=Post&gio_link_id=a9By01Oo?

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let once = false;
    return function(...args){
        temp = args;
        console.log(temp)
        if(once == false){
            var result = fn(...args);
            once = true;
            return result;
        }

    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */