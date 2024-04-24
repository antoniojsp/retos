//https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-04-24


class Solution {
public:
    int tribonacci(int n) {
        vector <int> dp = {0,1,1};
        for(int i = 2; i < n; i++){
            int temp = dp[i-2]+dp[i-1]+dp[i];
            dp.push_back(temp);
        }
        return dp[n];

    }
};