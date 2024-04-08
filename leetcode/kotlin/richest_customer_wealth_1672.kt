//https://leetcode.com/problems/richest-customer-wealth/description/



class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {

        var max_wealth: Int = 0

        for(amount in accounts){
            var suma: Int = amount.sum()
            max_wealth = if (suma > max_wealth) suma else max_wealth
        }

        return max_wealth

    }
}