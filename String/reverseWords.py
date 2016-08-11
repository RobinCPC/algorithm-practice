"""
#: 151
Title: Reverse Words in a String
Description:
------
 Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

Clarification:

    * What constitutes a word?
        A sequence of non-space characters constitutes a word.
    * Could the input string contain leading or trailing spaces?
        Yes. However, your reversed string should not contain leading or trailing spaces.
    * How about multiple spaces between two words?
        Reduce them to a single space in the reversed string.

------
Time: O(n)
Space: O(n)
Difficulty: Medium
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isspace():
            return ''
        str_list = s.split()
        str_list.reverse()
        return ' '.join(str_list)

if __name__ == '__main__':
    inp_str = '   the  sky is    blue '
    sol = Solution()
    print sol.reverseWords(inp_str)
    inp_str = '     '
    print sol.reverseWords(inp_str)

