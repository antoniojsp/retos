
//https://leetcode.com/problems/sleep/description/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {

     await new Promise((x) => {setTimeout(x, millis)});
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */