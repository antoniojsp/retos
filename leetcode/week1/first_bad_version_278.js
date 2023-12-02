/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {

    var start = 0
    var end = n
    while(start <= end){
        var mid  = Math.floor((start + end)/2);

        if (isBadVersion(mid) && !isBadVersion(mid-1)){
            return mid;
        }else if(!isBadVersion(mid)){
            start = mid + 1;
        }else if (isBadVersion(mid)){
            end = mid - 1;
        }
    };
        
    };
};