"""
#: 28
Title: Implement strStr()
Description:
------
 Implement strStr().

Returns the index of the first occurrence of needle in haystack, or
-1 if needle is not part of haystack.
------
Time: O(n*k)    # n = len(sentence), k = len(word)
Space: O(1)
Difficulty: Easy
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if len(haystack) < len(needle):
            return -1

        for i in xrange(len(haystack) - len(needle) + 1 ):
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else: # special else method : means 'no break'
            # if j == len(needle)-1:
                return i
        return -1
        #return haystack.find(needle)


"""
KMP algorithm
Time:   O(n+k)
Space:  O(k)    # need extra space for storage prefix
"""
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if len(haystack) < len(needle):
            return -1

        return self.KMP(haystack, needle)


    def KMP(self, text, pattern):
        """KMP algorithm for string match"""
        prefix = self.getPrefix(pattern)
        j = -1
        for i in xrange(len(text)):
            while j > -1 and pattern[j+1] != text[i]:
                j = prefix[j]
            if pattern[j+1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1



    def getPrefix(self, pattern):
        """get prefix for KMP algorithm"""
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j+1] != pattern[i]:
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix


if __name__ == '__main__':
    sol = Solution()
    print sol.strStr('abababcdab', 'babcda')
    sol2 = Solution2()
    print sol.strStr('helloworld','owo')

