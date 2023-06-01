/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */
//  0 1 2 3 4 5 6 7

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

        var start = 0;
        var end = n;

        while (start < end){
            mid = start + Math.floor((end - start)/2);

            if(isBadVersion(mid)){
                end = mid;
            }else{
                start = mid + 1;
            }
        }

        return start

    };
};