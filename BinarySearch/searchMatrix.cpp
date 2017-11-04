/*
* #: 74
* Title: Search a 2D Matrix
* Description:
* ------
*
* Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
*
*     Integers in each row are sorted from left to right.
*     The first integer of each row is greater than the last integer of the previous row.
*
* For example,
*
* Consider the following matrix:
*
* [
*   [1,   3,  5,  7],
*   [10, 11, 16, 20],
*   [23, 30, 34, 50]
* ]
*
* Given target = 3, return true.
*
* ------
* Time: O(log(mn))
* Space: O(1)
* Difficulty: Medium
*/
#include <iostream>
#include <vector>
#include <cassert>
using std::cout;
using std::endl;
using std::vector;


class Solution{
  public:
    bool searchMatrix(vector<vector<int>>& matrix, int target){
      // check corner case
      if(matrix.empty() || matrix[0].empty())
        return false;
      int row = matrix.size(), col = matrix.size();
      int start = 0, end = row*col-1;
      while(start <= end){
        int mid = start + (end-start)/2;
        int val = matrix[mid/col][mid%col];
        if (val == target)
          return true;
        else if(val > target){
          end = mid - 1;
        }else{
          start = mid +1;
        }
      }
      return false;
    }
};

int main(void)
{
  Solution sol = Solution();
  vector<vector<int>> mat{{ 1,  3,  5,  7},
                          {10, 11, 16, 20},
                          {23, 30, 34, 50}};
  int tar = 3;
  cout << sol.searchMatrix(mat, tar) << endl;
  assert(sol.searchMatrix(mat, tar) == true);
  return 0;
}

