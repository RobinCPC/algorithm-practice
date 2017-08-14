"""
#: 12
Title: Integer to Roman
Description:
------
Given an integer, convert it to a roman numeral.


Input is guaranteed to be within the range from 1 to 3999.
------
Time: O(n)
Space: O(1)
Difficulty: Medium
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        th = ["", "M", "MM", "MMM"]
        hu = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        te = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        di = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        res = th[num/1000] + hu[(num%1000)/100] + te[(num%100)/10] + di[num%10]
        return res


if __name__ == '__main__':
    sol = Solution()
    num = 3999
    assert sol.intToRoman(num) == "MMMCMXCIX", "Not correct!"

