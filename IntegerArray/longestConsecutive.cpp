/*
* #: 128
* Title: Longest Consecutive Sequence
* Description:
* ------
* Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
*
* For example,
* Given `[100, 4, 200, 1, 3, 2]`,
* The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.
*
* Your algorithm should run in O(n) complexity.
* ------
* Time: O(n)
* Space: O(n)
* Difficulty: Hard
*/
// Source: https://discuss.leetcode.com/topic/16483/a-simple-c-solution-using-unordered_set-and-simple-consideration-about-this-problem
// Use unordered_set (hash_table w/ O(1) lookup) to record all unique elements
// and look for previous and next continues numbers
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;


class Solution{
public:
    int longestConsecutive(vector<int>& nums){
        unordered_set<int> record(nums.begin(), nums.end());
        int result = 0;
        for(int n : nums){
            if(record.find(n) == record.end())
                continue;
            record.erase(n);
            int prev = n -1, next = n + 1;
            while(record.find(prev) != record.end())
                record.erase(prev--);
            while(record.find(next) != record.end())
                record.erase(next++);
            result = max( result, next - prev - 1);
        }
        return result;
    }
};



int main(void)
{
    vector<int> nums = {100, 1, 200, 3, 2, 4};
    Solution sol = Solution();
    cout << sol.longestConsecutive(nums) << endl;
    return 0;
}
