//https://leetcode.com/problems/roman-to-integer/submissions/
/**
 * @param {string} s
 * @return {number}
 */

const roman_numeral = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
};



var romanToInt = function(s) {

    var new_arr = Array.from(s).map(
        (x)=>roman_numeral[x]
    );

    let starting_value = new_arr.pop();
    var answer = starting_value;
    var prev = starting_value;

    while (0 < new_arr.length){
        let current = new_arr.pop();

        if ((prev == current) || (answer < current) ){
            answer += current;
        }else{
            answer -= current;
        }
        prev = current;
    };

    return answer;
};