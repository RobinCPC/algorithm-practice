/*
* #: 47
* Title: Permutation II
* Description:
* ------
* Given a collection of numbers that might contain duplicates, return all possible unique permutations.
*
* For example,
* [1,1,2] have the following unique permutations:
* ```
* [
*   [1,1,2],
*   [1,2,1],
*   [2,1,1]
* ]
* ```
* ------
* Time: O(n*n!)
* Space: O(n)
* Difficulty: Medium
*/
// TODO: Check Complexity


#include <iostream>     // cout
#include <vector>       // vector
#include <algorithm>    // sort
using std::vector;
using std::cout;


class Solution
{
public:
    vector<vector<int>> permuteUnique(vector<int> &nums)
    {
        if (nums.size() <= 1)
        {
            cout << nums.size();
            vector<vector<int>> ret{nums};
            return ret;
        }
        vector<vector<int>> per_grp{{}};
        for(auto val : nums)
        {
            vector<vector<int>> tmp_list;
            for(auto per : per_grp)
            {
                int n_len = per.size();
                for(int i=0; i < n_len+1; ++i)
                {
                    vector<int> tmp(per);
                    tmp.insert(tmp.begin()+i,val);
                    tmp_list.push_back(tmp);
                    if (i < n_len && per[i] == val)
                    {
                        break;
                    }
                }
            }
            per_grp=tmp_list;
        }
        std::sort(per_grp.begin(), per_grp.end());
        return per_grp;
    }
};

int main(void)
{
    Solution obj = Solution();
    vector<int> num_lst{1,1,2};
    auto ret = obj.permuteUnique(num_lst);
    //cout << "[\n";
//    for (std::vector<vector<int>>::iterator grp = ret.begin(); grp != ret.end(); ++grp) {
//        cout << '[';
//        for (std::vector<int>::iterator it = grp->begin(); it != grp->end(); ++it) {
//            cout << *it << ',';
//        }
//        cout << ']';
//    }
    //cout << "\n]\n";

    // range for loop
    for(auto row:ret)
    {
        cout << '[';
        for(auto col:row)
        {
            cout << col;
        }
        cout << ']';
    }

    return 0;
}
