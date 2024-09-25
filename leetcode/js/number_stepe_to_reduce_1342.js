/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {

    var count = 0;

    while (num > 0){
        count++;
        if (num%2==0){
            num = num/2;
        }else{
            num--;
        }
    }
    return count;
};