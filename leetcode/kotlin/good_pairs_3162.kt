
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Int {
        var res = 0

        for (i in nums1) {
            for (j in nums2) {
                if (i % (j * k) == 0) res++
            }
        }
        return res
    }
}