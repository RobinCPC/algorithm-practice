"""
#: 266
Title: Palindrome Permutation
Description:
------
Given a string, determine if a permutation of the string could form a palindrome.

For example,
```
"code" -> False, "aab" -> True, "carerac" -> True.
```
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtypeL bool
        """
        table = {}
        n_odd_cnt = 0
        for i in s:
            if i not in table:
                table[i] = 1
                n_odd_cnt += 1
            else:
                table[i] += 1
                n_odd_cnt += 1 if table[i]%2 else -1
        return n_odd_cnt <= 1



class Solution2(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtypeL bool
        """
        from collections import Counter
        table = Counter(s)
        n_odd_cnt = sum([v % 2 for v in table.values()])
        return n_odd_cnt <= 1;


if __name__ == '__main__':
    obj = Solution()
    ss = 'b.db'     #'carerac'
    obj2 = Solution2()
    ss2 = 'carerac..'
    print obj.canPermutePalindrome(ss)
    print obj2.canPermutePalindrome(ss2)

