
//https://leetcode.com/problems/harshad-number/

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {

        int temp = x;
        int sum = 0;
        while (1 <= temp){
            sum += temp%10;
            temp/= 10;
        }

        return (x%sum == 0) ?  sum : -1;
    }
};