/*
* #: 643
* Title: Maximum Average Subarray I
* Description:
* ------

Given an array consisting of n integers, find the contiguous subarray of given
length k that has the maximum average value. And you need to output the maximum
average value.


Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75



Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;


class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        long cum = 0;
        for(int i=0; i < k; ++i){
            cum += nums[i];
        }
        long max_val = cum;
        for(int i=k; i<n; ++i){
            cum = cum + nums[i] - nums[i-k];
            if (cum > max_val)
                max_val = cum;
        }
        return (double)max_val / k;
    }
};


int main(void)
{
    Solution sol = Solution();
    vector<int> nums {1, 12, -5, -6, 50, 3};
    int k = 4;
    assert(sol.findMaxAverage(nums, k) == 12.75);
    double output = sol.findMaxAverage(nums, k);
    cout << output;
    return 0;
}
