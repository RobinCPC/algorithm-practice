# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# time: 
# space: O(1) # constant, only need to declare 
# 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483648
        MIN_INT = -2147483648
        if x > -10 and x < 10:
            return x
        elif x >= 10:
            revX = int(str(x)[::-1])
            if revX > MAX_INT:
                return 0
            return revX
        else:
            xs = str(x)
            revX = -1*int(xs[1:][::-1])
            if revX < MIN_INT:
                return 0
            return revX

if __name__=='__main__':
    sol = Solution()
    n = -321
    print sol.reverse(n)

