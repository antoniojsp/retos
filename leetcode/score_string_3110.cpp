
//https://leetcode.com/problems/score-of-a-string/


class Solution {
public:
    int scoreOfString(string s) {
        int i = 0;
        int result = 0;
        while(i < s.size()-1){
            result += abs(int(s[i]) - int(s[i+1]));
            i++;
        }

        return result;
    }
};