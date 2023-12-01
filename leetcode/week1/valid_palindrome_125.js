/**
 * @param {string} s
 * @return {boolean}
 */
function atRange(char, low, high){
    var ascii_value = char.charCodeAt(0);
    return ascii_value >= low && ascii_value <= high;
};

var isPalindrome = function(s) {
    var temp = s.toLowerCase();
    var result = []

    for (let i of temp){
        // 97-122 -> alpha, 48-57 -> numeric
        if (atRange(i, 97,122) || atRange(i, 48, 57)){
            result.push(i)
        }
    }

    return result.join("") == result.reverse().join("");

};