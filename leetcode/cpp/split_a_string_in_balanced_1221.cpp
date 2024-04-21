//https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

class Solution {
public:
    int balancedStringSplit(string s) {

        int r = 0;
        int l = 0;
        int count = 0;
        for (char i: s){
            if (i == 'R'){
                r++;
            }else{
                l++;
            }

            if (r == l){
                r = 0;
                l = 0;
                count++;
            }
        }

        return count;
    }
};