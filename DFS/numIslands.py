"""
#: 200
Title: Number of Islands
Description:
------
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
11110
11010
11000
00000
```
Answer: 1

Example 2:
```
11000
11000
00100
00011
```
Answer: 3
------
Time: O(n)
Space: O( 1)
Difficulty: Medium
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n_islands = 0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                if grid[r][c] == '1':
                    self.visitIsland(r,c,grid)
                    n_islands += 1
        return n_islands


    def visitIsland(self, row, col, matrix):
        if row >= 0 and row < len(matrix) and col >=0 and col < len(matrix[0]) and matrix[row][col] == '1':
            matrix[row][col] = 'm'
            self.visitIsland(row-1, col, matrix)
            self.visitIsland(row+1, col, matrix)
            self.visitIsland(row, col-1, matrix)
            self.visitIsland(row, col+1, matrix)


if __name__ == '__main__':
    island = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]
    sol = Solution()
    print sol.numIslands(island)

