"""
#: 8
Title: String to Integer (atoi)
Description:
------
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        str = str.strip()
        rint = 0
        sign = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]

        for i in str:
            if  48 <= ord(i) <= 57:
                rint = rint*10 + (ord(i) - 48)*sign
                if rint >= 2**31:
                    rint = 2**31 - 1
                elif rint <= -2**31:
                    rint = -2**31
            elif ord(i) == 46:
                break;
            else:
                return rint #0
        return rint

if __name__ == '__main__':
    print Solution().myAtoi("")
    print Solution().myAtoi("-1")
    print Solution().myAtoi("2147483647")
    print Solution().myAtoi("2147483648")
    print Solution().myAtoi("-2147483648")
    print Solution().myAtoi("-2147483649")

