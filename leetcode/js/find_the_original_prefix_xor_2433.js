//#https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/


/**
 * @param {number[]} pref
 * @return {number[]}
 */
var findArray = function(pref) {

    var temp = pref[0];

    for(let i = 1; i<pref.length; i++){
        pref[i] = temp ^pref[i];
        temp = temp ^ pref[i];
    }

    return pref;
};