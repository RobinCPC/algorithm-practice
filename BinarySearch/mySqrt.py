"""
#: 69
Title: Sqrt(x)
Description:
------
Implement `int sqrt(int x)`.

Compute and return the square root of x.
------
Time: O(log(n))
Space: O(1)
Difficulty: Medium
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
        l, r = x, 0
        res = 1
        dif = float('inf')
        while l-r > 1:
            m = (l+r)/2
            if m**2 > x:
                l = m
            elif m**2 < x:
                tmp = x - m**2
                if tmp < dif:
                    res = m
                    dif = tmp
                    r = m
            else:
                res,l,r = m, m, m
                dif = 0
        return res


    # Integer Newton
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r > x / r:
            r = (r + x/r) / 2
        return r


if __name__ == '__main__':
    obj = Solution()
    inp = 11
    print obj.mySqrt(inp)
    print obj.mySqrt2(inp)


