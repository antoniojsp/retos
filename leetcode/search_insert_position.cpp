
//https://leetcode.com/problems/search-insert-position/description/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        int answer = 0;
        while (start <= end){
            int mid = start + (end-start)/2;
            if(nums[mid] == target){
                answer = mid;
                break;
            }else if (nums[mid] < target){
                answer = mid+1;
                start = mid + 1;
            }else if (nums[mid] > target){
                answer = mid;
                end = mid - 1;
            }
        };
        return answer;
    }
};