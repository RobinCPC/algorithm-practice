/*
* #: 118
* Title: Pascal's Triangle
* Description:
* ------
* Given numRows, generate the first numRows of Pascal's triangle.
*
*
* For example, given numRows = 5,
* Return
* ```
* [
*      [1],
*     [1,1],
*    [1,2,1],
*   [1,3,3,1],
*  [1,4,6,4,1]
* ]
* ```
* ------
* Time: O(n)
* Space: O(n)
* Difficulty: Easy
*/

#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res={};
        if (numRows == 0)
            return res;
        res.push_back(vector<int>{1});
        if (numRows == 1)
            return res;
        res.push_back(vector<int>{1,1});
        if (numRows == 2)
            return res;
        for( int i=2; i < numRows; ++i){
            vector<int> tmp{1};
            for(int j=1; j < i; ++j){
                tmp.push_back( res[i-1][j-1] + res[i-1][j]);
            }
            tmp.push_back(1);
            res.push_back(tmp);
        }
        return res;
    }
};


int main(void)
{
    Solution sol = Solution();
    int numRows = 5;
    vector<vector<int>> res = sol.generate(numRows);
    for(vector<int> i : res){
        cout << "[ ";
        for(auto j : i){
            cout << j << ' ';
        }
        cout << "]\n";
    }
    return 0;
}
