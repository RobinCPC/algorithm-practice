"""
#: 118
Title: Pascal's Triangle
Description:
------
Given numRows, generate the first numRows of Pascal's triangle.


For example, given numRows = 5,
Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```
------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        n1 = [1]
        n2 = [1,1]
        res = [n1, n2]
        if numRows == 1:
            return [n1]
        elif numRows == 2:
            return res
        else:
            for i in xrange(2, numRows):
                tmp = [1]
                for j in xrange(1, i):
                    tmp.append( res[i-1][j-1] + res[i-1][j])
                tmp.append(1)
                res.append(tmp)
            return res


if __name__ == '__main__':
    sol = Solution()
    numRows = 9
    print sol.generate(numRows)

