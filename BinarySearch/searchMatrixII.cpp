/*
* #: 240
* Title: Search a 2D Matrix II
* Description:
* ------
*
* Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
*
*     Integers in each row are sorted in ascending from left to right.
*     Integers in each column are sorted in ascending from top to bottom.
*
* For example,
*
* Consider the following matrix:
*
* [
*   [1,   4,  7, 11, 15],
*   [2,   5,  8, 12, 19],
*   [3,   6,  9, 16, 22],
*   [10, 13, 14, 17, 24],
*   [18, 21, 23, 26, 30]
* ]
*
* Given target = 5, return true.
*
* Given target = 20, return false.
*
* ------
* Time: O(m+n)
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
      //test corner case
      if(matrix.empty() || matrix[0].empty())
        return false;
      int row = matrix.size(), col = matrix[0].size();
      int i = 0, j = col-1;
      while(i < row && j >=0){
          if(matrix[i][j] == target)
              return true;
          else if(matrix[i][j] < target){
              i++;
          }else if(matrix[i][j] > target){
              j--;
          }
      }
      return false;
    }

    bool searchMatrix2(vector<vector<int>>& matrix, int target){
      /* time: O(mlog(n) */
      // check corner
      if(matrix.empty() || matrix[0].empty())
        return false;
      for(size_t i=0; i < matrix.size(); ++i){
        if(searchVector(matrix[i], target)) return true;
      }
      return false;
    }

    bool searchVector(vector<int>& vec, int tar){
      int s = 0, e = vec.size() -1;
      while(s <= e){
        int m = s + (e-s)/2;
        int val = vec[m];
        if( val == tar)
          return true;
        else if(val < tar)
          s = m + 1;
        else
          e = m -1;
      }
      return false;
    }
};

int main(void)
{
  Solution sol = Solution();
  vector<vector<int>> mat{{1,   4,  7, 11, 15},
                          {2,   5,  8, 12, 19},
                          {3,   6,  9, 16, 22},
                          {10, 13, 14, 17, 24},
                          {18, 21, 23, 26, 30}
                         };
  int tar = 13;
  cout << sol.searchMatrix2(mat, tar) << endl;
  assert(sol.searchMatrix(mat, 20) == false);
  return 0;
}
