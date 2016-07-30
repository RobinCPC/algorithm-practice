/*
* #: 189
* Title: Rotate Array
* Description:
* ------
* Rotate an array of n elements to the right by k steps.
* For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
* Note:
* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* Hint:
* Could you do it in-place with O(1) extra space?
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/

#include <iostream>     // cout
#include <vector>       // vector
#include <algorithm>    // reverse, iter_swap

using std::vector;

class Solution
{
public:
    void rotate(vector<int>& nums, int k)    // 70ms
    {
        if (k!=0 && nums.size() > 1)
        {
            k %= nums.size();
            for (; k > 0; --k)
            {
                auto p_num = nums.back();
                nums.pop_back();
                nums.insert(nums.begin(), p_num);
            }
        }
    }

    void rotate_alg(vector<int>& nums, int k)   // 20ms
    {
        if (!nums.empty())
        {
            k %= nums.size();
            std::reverse(nums.begin(), nums.begin() + nums.size()-k );
            std::reverse( nums.begin() + nums.size()-k, nums.end());
            std::reverse( nums.begin(), nums.end());
        }
    }

};

class Solution2
{
public:
    void rotate(vector<int>& nums, int k)
    {
        if(k>0 && nums.size()>1)
        {
            k %= nums.size();
            reverse(nums.begin(), nums.begin() + nums.size()-k );
            reverse( nums.begin() + nums.size()-k, nums.end());
            reverse( nums.begin(), nums.end());
        }
    }

private:
    void reverse(vector<int>::iterator begin, vector<int>::iterator end)
    {
        while (begin != end && begin != --end)
        {
            std::iter_swap(begin, end);
            ++begin;
        }
    }

};

int main(int argc, const char *argv[])
{
    Solution sol = Solution();
    vector<int> nums = {1,2,3,4,5,6,7};
    int k = 3;
    sol.rotate_alg(nums, k);
    std::cout << "nums = " << std::endl;
    for (auto it = nums.begin(); it != nums.end(); ++it) {
        std::cout << ' '<< *it;
    }
    std::cout << '\n';

    k = 4;
    Solution2 sol2 = Solution2();
    sol2.rotate(nums, k);
    std::cout << "nums = " << '\n';
    for (auto it = nums.begin(); it != nums.end(); ++it) {
        std::cout << ' ' << *it;
    }
    std::cout << '\n';


    return 0;
}
