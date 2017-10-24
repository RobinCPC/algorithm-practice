/*
 #: 53
 Title: Maximum maxSubArray
 Description:
 ------
  Find the contiguous subarray within an array (containing at least one number)
  which has the largest sum.
 
  For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
  the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 ------
 Time: O(n)
 Space: O(1)
 Difficulty: Easy
*/
#include <iostream>
#include <vector>
#include <climits>
using std::vector;
using std::cout;
using std::endl;

class Solution {
    public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        if(nums.size()==0)
            return maxSum; 
        else if(nums.size()==1)
            return nums[0];
        int curSum = nums[0];
        for(size_t i=1; i < nums.size(); ++i){
            curSum = nums[i] > curSum+nums[i] ? nums[i]:curSum+nums[i];
            maxSum = curSum > maxSum ? curSum: maxSum;
        }
        return maxSum;
    }
};


int main(void)
{
    Solution sol = Solution();
    vector<int> n{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << sol.maxSubArray(n);
    return 0;
}
