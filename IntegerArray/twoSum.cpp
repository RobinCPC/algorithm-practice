/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

------

twoSum_array:
Time: O(n^2)
Space: O(1) # no extra space needed

Time: O(n)
Space:O(n)  # need extra space for hash table
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum_array(vector<int>& nums, int target) {
        vector<int> ind;
        for (int i=0; i < nums.size(); ++i) // first loop: choose 1st number
        {
            int rem_tar = target - nums[i];
            for (int j = i+1; j < nums.size(); ++j)
            {
                if( nums[j] == rem_tar) // find next numebr
                {
                    ind.push_back(i);
                    ind.push_back(j);
                    return ind;
                }
            }
        }
        vector<int> fa(2,-1);
        return fa;
    }
};

int main()
{
    Solution sol = Solution();
    int tar = 0;
    int arr[] = {0, 3, 2, 1};
    vector<int> nums( arr, arr + sizeof(arr)/sizeof(int));

    vector<int> ind = sol.twoSum_array(nums, tar);
    for (vector<int>::iterator it = ind.begin(); it !=ind.end() ; ++it )
    {
        cout << *it << '\t';
    }
    cout << endl;
    return 0;
}
