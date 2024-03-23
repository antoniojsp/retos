
//https://leetcode.com/problems/add-two-promises/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // const [one, two] = await Promise.all([promise1, promise2]);
    var one = await promise1;
    var two =  await promise2;
    return one+two;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */