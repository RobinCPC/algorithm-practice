"""
#: 190
Title: Reverse Bits
Description:
------
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
                 return 964176192 (represented in binary as 00111001011110000010100101000000).


Follow up:
If this function is called many times, how would you optimize it?


Related problem: Reverse Integer

Credits:Special thanks to @ts for adding this problem and creating all test cases.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """bit manipulate"""
        res = 0
        for i in range(0,32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res


    def reverseBits1(self, n):
        """ math """
        b_n = bin(n)
        pre_digit = 32 - len(b_n[2:])
        res = 0
        for ind, e in enumerate(b_n[2:]):
            res += (2**(ind+pre_digit)) * int(e)
        return res


    def reverseBits2(self, n):
        """ python """
        s = bin(n)[2:]
        s = str((32-len(s))*'0' + s)
        s = s[::-1]
        return int(s, 2)


if __name__ == '__main__':
    sol = Solution()
    n = 43261596
    print bin(n)
    res = sol.reverseBits2(n)
    print bin(res)
    print res

