"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

time: O(n)
space: O(1) 
"""
class Solution(object):
    def titleToNumber2(self, s): # 68 ms (use ** operator will be 104 ms)
        """
        :type s: str
        :rtype: int
        """
        num = 0
        digit = len(s) - 1
        for i in s:
            num += pow(26,digit) * ( ord(i) - 64 )
            digit -= 1
        return num

    def titleToNumber(self, s): # still 68 ms (without pow) 
        """
        :type s: str
        :rtype: int
        """
        num = 0
        digit = len(s) - 1
        for i in s:
            num = num*26 + ( ord(i) - 64 )
            digit -= 1
        return num
        
if __name__ == '__main__':
    sol = Solution()
    s = 'AA'
    print sol.titleToNumber(s)
    print sol.titleToNumber('GQ')
    print sol.titleToNumber('BXZ')
    print sol.titleToNumber('Z')

