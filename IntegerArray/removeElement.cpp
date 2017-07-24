/*
* #: 27
* Title: Remove Element
* Description:
* ------
* Given an array and a value, remove all instances of that value in place and return the new length.
*
* Do not allocate extra space for another array, you must do this in place with constant memory.
*
* The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*
* Example:
* Given input array nums = `[3,2,2,3]`, val = `3`
*
* Your function should return length = 2, with the first two elements of nums being 2.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int h = 0;
        int t = nums.size();
        while (h < t){
            if( nums[h] == val){
                nums[h] = nums[t - 1];
                t--;
            }else{
                h++;
            }
        }
        return t;
    }
};

int main(void)
{
    Solution sol = Solution();
    vector<int> nums = {4,1,2,3,5};
    int val = 4;
    unsigned int len = sol.removeElement(nums, val);
    for(unsigned int i=0; i<len; ++i){
        cout << nums[i] << ' ';
    }
    return 0;
}
