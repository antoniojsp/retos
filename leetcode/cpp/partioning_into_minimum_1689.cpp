
//https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

class Solution {
public:
    int minPartitions(string n) {

        int max_digit = 0;

        for (int i = 9; i>0; i--){
            if (n.find(to_string(i)) != string::npos) {
                max_digit = i;
                break;
            }
        }

        return max_digit;
    }

};