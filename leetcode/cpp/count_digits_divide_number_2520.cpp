
//https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

class Solution {
public:
    int countDigits(int num) {

        int digits = num;
        int count = 0;
        while (digits >= 1){
            int digit = digits%10;
            if(num % digit==0){
                count++;
            }
            digits/=10;
        }

        return count;
    }
};