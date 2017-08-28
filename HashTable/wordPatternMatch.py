"""
#: 291
Title: Word Pattern II
Description:
------

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:

    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aaaa", str = "asdasdasdasd" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:
You may assume both pattern and str contains only lowercase letters.

------
Time: O(?)
Space: O(?)
Difficulty: Hard
"""
# TODO: Check Complexity
#source:  https://discuss.leetcode.com/topic/28340/python-backtracking-48ms/8
# others: http://www.cnblogs.com/Dylan-Java-NYC/p/6351250.html
#         http://www.jianshu.com/p/27e3ab842761
#         https://repl.it/CekC/1
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) > len(str):
            return False
        else:
            return self.helper(pattern, str, {}, {})

    def helper(self, pattern, string, pTable={}, sTable={}):
        """
        :type pattern: str
        :type string: str
        :type pTable: dict
        :type sTable: dict
        :rtype: bool
        """
        if not pattern and string:
            return False
        if not pattern and not string:
            print pTable.items()
            return True

        # === main part of backtracking ===
        # abcde redblue
        # ^xxxx ^^^xxxx
        #   5       7
        # Try to match pattern `a` with at most 3 characters.
        # That is 7 - 5 + 1, and the last + 1 is for Python range.
        for end in xrange(1, (len(string) - (len(pattern) - 1) + 1)):
            p, s = pattern[0], string[:end]
            # if is a new pattern
            if p not in pTable and s not in sTable:
                pTable[p] = s
                sTable[s] = p
                # see if new pattern correct or not
                print "new pattern, {%s}, {%s}" % (p, s)
                if self.helper(pattern[1:], string[end:], pTable, sTable):
                    return True
                # not correct, then backtrack and try next pattern
                #print "new pattern2"
                del pTable[p]
                del sTable[s]
            # if is old pattern
            elif p in pTable and pTable[p] == s:
                # search next pattern
                print "old pattern, {%s}, {%s}" % (p, s)
                if self.helper(pattern[1:], string[end:], pTable, sTable):
                    return True
                # not correct
                #print "old pattern2"
                pass
            else:
                # Invalid, but we need to do try next pattern. so not return yet.
                print "either, {%s}, {%s}" % (p, s)
                pass
        return False

if __name__ == '__main__':
    sol = Solution()
    assert sol.wordPatternMatch("abab", "reblrebl") == True, "must be True"
    #assert sol.wordPatternMatch("aaaa", "asdasdasdasd") == True, "must be True"
    #assert sol.wordPatternMatch("aabb", "xyzabcxzyabc") == False, "must be False"
