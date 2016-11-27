"""
#: 70
Title: Climb Stairs
Description:
------
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:      # only one way for both 0 & 1 stairs
            return 1
        n_step = [1, 1] # record numbers of way from previous two steps
        n_way = 0
        step = 2        # star from 2 steps
        while step <= n:
            n_way = n_step[0] + n_step[1]   # get ways from n-1 and n-2 steps
            n_step.pop(0)
            n_step.append(n_way)            # only record previos two step.
            step += 1
        return n_way


if __name__ == '__main__':
    obj = Solution()
    steps = 10
    print obj.climbStairs(steps)


