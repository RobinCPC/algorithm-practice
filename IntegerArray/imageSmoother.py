"""
#: 661
Title: Images Smoother
Description:
------
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
```
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```
Note:

    The value in the given matrix is in the range of [0, 255].
    The length and width of the given matrix are in the range of [1, 150].

------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        out = [ [ 0 for _j in M[0]] for _i in M]
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        for x in xrange(x_len):
            for y in xrange(y_len):
                surrond = [M[i][j]
                           for i in (x-1, x, x+1)
                           for j in (y-1, y, y+1)
                           if 0 <= i < x_len and 0 <= j < y_len]
                out[x][y] = sum(surrond) // len(surrond)
        return out

if __name__ == '__main__':
    M = [[1,5,1], [1, 7, 1], [3, 1, 1]]
    sol = Solution()
    print sol.imageSmoother(M)
    assert sol.imageSmoother(M) == [[3,2,3], [3,2,2], [3,2,2]], "Not Correct!"

