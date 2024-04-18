

//https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {

        vector <int> copy = nums;
        int max_val = *max_element(copy.begin(),copy.end());
        int hash_map[max_val+2];
        memset(hash_map, 0, sizeof(hash_map));

        for(int i = 0; i<copy.size(); i++){
            hash_map[copy[i]+1] += 1;
        }

        for(int i = 1; i<sizeof(hash_map)/sizeof(int); i++){
            hash_map[i] += hash_map[i-1];
        }

        for(int i = 0; i<copy.size();i++){
            copy[i] = hash_map[copy[i]];
        }
        return copy;
    }
};