"""
#: 205
Title: Isomorphic Strings
Description:
------
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t = {} # a hash table map s to t
        used = set()
        for i in xrange(len(s)):
            if s[i] not in s2t and t[i] not in used:
                s2t[s[i]] = t[i]
                used.add(t[i])
            elif (s[i] not in s2t and t[i] in used) or (s[i] in s2t and t[i] not in used):
                return False
            else:
                if s2t[s[i]] != t[i]:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = 'egg'
    t = 'add'
    print sol.isIsomorphic(s,t)

