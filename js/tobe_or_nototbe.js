//https://leetcode.com/studyplan/30-days-of-javascript/

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {

    const ToBe = (x) => {
        if(x===val){
            return true;
        }
        throw new Error("Not Equal")

    }

    const NotToBe =  (x) =>{
        if(x!==val){
            return true;
        }
        throw new Error("Equal")

    }

  return {toBe:ToBe,
          notToBe:NotToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */