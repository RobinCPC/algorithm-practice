"""
#: 13
Title: Roman to Integer
Description:
------
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""
# source: https://discuss.leetcode.com/topic/17110/my-straightforward-python-solution
# Note: The trick is that the last letter is always added. Except the last one,
# if one letter is less than its latter one, this letter is subtracted.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2i = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        for e in xrange(len(s)-1):
            if r2i[s[e]] < r2i[s[e+1]]:
                res -= r2i[s[e]]
            else:
                res += r2i[s[e]]
        res += r2i[s[-1]]
        return res


if __name__ == "__main__":
    sol = Solution()
    romstr = "MMMCMXCIX"
    print sol.romanToInt(romstr)
    assert sol.romanToInt(romstr) == 3999, "Not correct!"

