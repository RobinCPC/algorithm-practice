"""
#: 49
Title: Group Anagrams
Description:
------
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]

Note: All inputs will be in lower-case.
------
Time: O(2nLlogL)    # N is # of input string, L is average lenght of string
Space: O(n)
Difficulty: Medium
"""

import collections

class Solution(object):
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 2:
            return [strs]
        sort_table = collections.defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            sort_table[ss].append(s)
        return sort_table.values()


if __name__ == '__main__':
   inp_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
   sol = Solution()
   print sol.groupAnagrams(inp_str)

