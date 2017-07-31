/*
* #: 217
* Title: Contains Duplicate
* Description:
* ------
*
* Given an array of integers, find if the array contains any duplicates. Your
* function should return true if any value appears at least twice in the array,
* and it should return false if every element is distinct.
*
* ------
* Time: O(n)
* Space: O(n)
* Difficulty: Easy
*/
#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;

class Solution{
    public:
        bool containsDuplicate(vector<int>& nums){
            return nums.size() > set<int>(nums.begin(), nums.end()).size();
        }

        bool containsDuplicate1(vector<int>& nums) {
            unordered_set<int> hash_set {};
            for (auto e : nums){
                if (hash_set.find(e) != hash_set.end()){
                    return true;
                }else{
                    hash_set.insert(e);
                }
            }
            return false;
        }
};

int main(void)
{
    Solution sol = Solution();
    vector<int> nums {1,2,3,4,6,5,8,7,8,3,9, 10};
    cout << sol.containsDuplicate(nums) << endl;
    vector<int> nums2 {1,2,3,4,5};
    cout << sol.containsDuplicate(nums2) << endl;
    return 0;
}
