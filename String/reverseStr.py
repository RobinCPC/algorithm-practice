"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString_build(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        else:
            s_lt = list(s)
            for i in xrange(n//2):
                s_lt[i], s_lt[-i-1] = s_lt[-i-1], s_lt[i]
            return "".join(s_lt)



if __name__ == '__main__':
    sol = Solution()
    print sol.reverseString_build('hello')
    print sol.reverseString('world')

