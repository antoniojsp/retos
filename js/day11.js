/**
 * @param {number} millis
 */
async function sleep(millis) {
    // await new Promise(o => setTimeout(o, millis));
    return new Promise(o => setTimeout(o, millis));
};


/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */