"""
#: 55   # lintcode
Title: Compare Strings
Description:
------
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.
------
Time: O(2n)
Space: O(1)
Difficulty: Easy
"""

import collections

class Solution(object):
    """docstring for Solution"""
    def compare_strings(self, A, B):
        # return a dict with value set to 0
        letters = collections.defaultdict(int)
        for a in A:
            letters[a] += 1

        for b in B:
            if b not in letters:
                return False
            elif letters[b] <= 0:
                return False
            else:
                letters[b] -= 1
        return True


if __name__ == '__main__':
    strA = 'ABCD'
    strB = 'ABC'
    strC = 'AABC'
    sol = Solution()
    print sol.compare_strings(strA, strB)
    print sol.compare_strings(strA, strC)

