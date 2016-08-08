"""
#: 125
Title: Valid Palindrome
Description:
------
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        start = 0
        end = len(s)-1
        is_pal = True
        while start < end:
            while (start < end) and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while (start < end) and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start >= end:
                break
            else:
                if s[start].lower() != s[end].lower():
                    is_pal = False
            start += 1
            end -= 1
        return is_pal

if __name__ == '__main__':
    sol = Solution()
    inp_str = "A man, a plan, a canal: Panama"
    print "str1 : \n", inp_str
    print "Is valid Palindrome?"
    print sol.isPalindrome(inp_str)

    inp_str2 = "race a care"
    print "str2 : \n", inp_str2
    print "Is valid Palindrome?"
    print sol.isPalindrome(inp_str2)

