"""
#: 67
Title: Add Binary
Description:
------
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""
import imp
tf = imp.load_source('timing_function', '../timing_function.py')


class Solution(object):
    @tf.timing_function
    def addBinary(self, a, b):
        """
        use python built-in  function
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    @tf.timing_function
    def addBinary0(self, a, b):
        """
        use string manipulate and math
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, c = len(a) - 1, len(b) - 1, 0
        out = ''
        while i >= 0 or j >= 0 or c == 1:
            if i >= 0:
                c += 1 if a[i] == '1' else 0
                i -= 1
            if j >= 0:
                c += 1 if b[j] == '1' else 0
                j -= 1
            out = str(c % 2) + str(out)
            c /= 2
        return out

if __name__ == '__main__':
    sol = Solution()
    bin1 = "111"
    bin2 = "11"
    assert sol.addBinary(bin1, bin2) == "1010", "Not Correct!"
    assert sol.addBinary0(bin1, bin2) == "1010", "Not Correct!"
