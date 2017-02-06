/*
* #: 200
* Title: Number of Islands
* Description:
* ------
* Given a 2d grid map of '1's (land) and '0's (water), count the number of 
* islands. An island is surrounded by water and is formed by connecting adjacent 
* lands horizontally or vertically. You may assume all four edges of the grid 
* are all surrounded by water.
* 
* Example 1:
* 
* 11110
* 11010
* 11000
* 00000
* Answer: 1
* 
* Example 2:
* 
* 11000
* 11000
* 00100
* 00011
* Answer: 3
* ------
* Time: O(n)
* Space: O( 1)
* Difficulty: Medium
*/
#include <iostream>
#include <vector>
using std::vector;
using std::cout;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n_islands = 0;
        for (size_t i=0; i < grid.size(); ++i){
            for (size_t j=0; j < grid[0].size(); ++j){
                if (grid[i][j] == '1') {
                    visitIsland(i, j, grid);
                    n_islands += 1;
                }
            }
        }
        return n_islands;
    }


    void visitIsland(const int row, const int col, vector<vector<char>>& matrix) {
        if ((row >=0) && (row < matrix.size()) && (col >= 0) and 
            (col < matrix[0].size()) and (matrix[row][col] == '1')){
                matrix[row][col] = 'm';
                visitIsland(row-1, col, matrix);
                visitIsland(row+1, col, matrix);
                visitIsland(row, col-1, matrix);
                visitIsland(row, col+1, matrix);
            }
        return;
    }
};


int main(void)
{
    vector<vector<char>> island = {{'1', '1', '0', '0', '0'},
                                   {'1', '1', '0', '0', '0'},
                                   {'0', '0', '1', '0', '0'},
                                   {'0', '0', '0', '1', '1'}};   
    Solution sol = Solution();
    cout << sol.numIslands(island);

    return 0;
}
