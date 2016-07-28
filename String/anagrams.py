"""
#: 242
Title: Valid Anagram
Description:
------
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
------
Time: O(n)
Space: O(1) # const 256 element of list
Difficulty: Easy
"""

class Solution(object):
    def anagrams_buildIn(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def anagrams_buildIn2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        return collections.Counter(s) == collections.Counter(t)

    def anagrams(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        cnt_char = [0]*256
        # ord to get ascii code (chr, unichr are the inverse function)
        for i in xrange( len(s) ):
            cnt_char[ ord(s[i]) ] += 1
            cnt_char[ ord(t[i]) ] -= 1
        for j in xrange( len(cnt_char) ):
            if cnt_char[j] != 0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.anagrams('hello !world', 'dlrow! olleh')

