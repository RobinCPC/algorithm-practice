/*
 * #: 238
 * Title: Product of Array Except Self
 * Description:
 * ------

 Given an array of n integers where n > 1, nums, return an array output such that
 output[i] is equal to the product of all the elements of nums except nums[i].

 Solve it without division and in O(n).

 For example, given [1,2,3,4], return [24,12,8,6].

 Follow up:
 Could you solve it with constant space complexity? (Note: The output array does
 not count as extra space for the purpose of space complexity analysis.)

 * ------
 * Time: O(n)
 * Space: O(1)
 * Difficulty: Medium
 */
#include <iostream>
#include <vector>
using namespace std;


class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int n = nums.size();
            //vector<int> output(n,1);  // create a vector of n length w/ all 1
            vector<int> output = {1};
            int tmp = 1;
            for (int i=1; i < n; ++i){
                tmp *= nums[i-1];
                output.push_back(tmp);
            }
            tmp = 1;
            for (int i = n-2; i >= 0; --i){
                tmp *= nums[i+1];
                output[i] *= tmp;
            }
            return output;
        }
};


int main(void)
{
    vector<int> nums {4,3,2,1,2};
    Solution sol = Solution();
    vector<int> output = sol.productExceptSelf(nums);
    for(auto i : output){
        cout << i << ' ';
    }
    return 0;
}
