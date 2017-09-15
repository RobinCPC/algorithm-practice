"""
#: 20
Title: Valid Parentheses
Description:
------
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        l_paren = ['(', '[', '{']
        r_paren = [')', ']', '}']
        stack_lst = []
        for i in s:
            if i in l_paren:
                stack_lst.append(i)
            elif i in r_paren:
                ind = r_paren.index(i)
                if len(stack_lst) != 0 and stack_lst[-1] == l_paren[ind]:
                    stack_lst.pop()
                else:
                    return False
            else:
                continue

        if len(stack_lst) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isValid("([)]")
    print Solution().isValid("(1[2]){3}")

