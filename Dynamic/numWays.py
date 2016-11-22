"""
#: 276
Title: Paint Fence
Description:
------
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        p_same = k*1
        p_diff = k*(k-1)
        for i in xrange(3,n+1):
            p_same, p_diff = p_diff * 1, (p_same + p_diff) * (k-1)
        return p_same + p_diff


if __name__ == '__main__':
    obj = Solution()
    n,k = 5,6
    print obj.numWays(n, k)

