"""
#: 79
Title: Longest Common Substring
Description:
------
Given two strings, find the longest common substring.
Return the length of it.

Example
Given A="ABCD", B="CBCE", return 2.
Note
The characters in substring should occur continuously in original string.
This is different with subsequence
------
Time: O(mn*lcs)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def longestCommonSubstring(self, A, B):
        """
        :type A: string
        :type B: string
        :rtype : int
        """
        if len(A)==0 or len(B)==0:
            return 0;
        lcs, lcs_tmp = 0, 0
        for i in xrange(len(A)):
            lcs_tmp = 0
            for j in xrange(len(B)):
                while i+lcs_tmp < len(A) and\
                      j+lcs_tmp < len(B) and\
                      A[i+lcs_tmp] == B[j+lcs_tmp]:
                    lcs_tmp +=1

                # update lcs
                if lcs_tmp > lcs:
                    lcs = lcs_tmp

        return lcs

if __name__ == '__main__':
    sol = Solution()
    strA = 'ABCD'
    strB = 'CBCE'
    print sol.longestCommonSubstring(strA, strB)

