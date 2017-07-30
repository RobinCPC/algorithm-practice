"""
#: 191
Title: Number of 1 Bits
Description:
------
Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
so the function should return 3.

Credits:Special thanks to @ts for adding this problem and creating all test cases.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        '&' with 1 and shift bit
        :type n: int
        :rtype: int
        """
        res = 0
        while(n):
            if n & 1:
                res += 1
            n = n >> 1
        return res


    def hammingWeight1(self, n):
        """
        use `n & n-1` trick
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt


if __name__ == '__main__':
    sol = Solution()
    num = 2**32 - 1  # max unsigned int
    print num, hex(num), bin(num)
    assert sol.hammingWeight(num) == 32, "not correct!"
    print sol.hammingWeight(num)
    print sol.hammingWeight1(num)

