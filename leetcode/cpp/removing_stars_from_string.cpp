https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <cstring>
class Solution {
public:
    string removeStars(string s) {
        char *stack = new char[s.size()+1];
        strcpy(stack, s.c_str());
        int i = 0;
        int j = 0;
        while (i < s.size()){
            if (s[i]=='*'){
                j-=1;
            }
            else{
                stack[j] = s[i];
                j+=1;
            }
            i++;
        }

        string answer = "";
        for (auto k = 0; k<=j-1;k++){
            answer+=stack[k];
        }

        return answer;
    }
};