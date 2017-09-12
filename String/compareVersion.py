"""
#: 165
Title: Compare Version Numbers
Description:
------
Compare two version numbers version1 and version2.
If version1 &gt; version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
`
0.1 < 1.1 < 1.2 < 13.37
`

Credits:Special thanks to @ts for adding this problem and creating all test cases.
------
Time: O(n)
Space: O(n)
Difficulty: Medium
"""
import imp
import os
cwd = os.getcwd()
tf = imp.load_source('timing_function', '../timing_function.py')


# reference: https://discuss.leetcode.com/topic/80000/python-solution-with-detailed-explanation
class Solution(object):
    @tf.timing_function
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        N = max(len(v1), len(v2))
        for i in xrange(N):
            e1 = int(v1[i]) if i < len(v1) else 0
            e2 = int(v2[i]) if i < len(v2) else 0
            if e1 > e2:
                return 1
            elif e1 < e2:
                return -1
        return 0


    @tf.timing_function
    def compareVersion0(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            v2 += [0]*(len(v1) - len(v2))
        elif len(v1) < len(v2):
            v1 += [0]*(len(v2) - len(v1))
        lev = 0
        len1 = len(v1)
        while lev < len1:
            if int(v1[lev]) > int(v2[lev]):
                return 1
            elif int(v1[lev]) < int(v2[lev]):
                return -1
            lev += 1
        return 0


if __name__ == '__main__':
    sol = Solution()
    ver1 = '2.3.15.00.0.0000.0.1'
    ver2 = '2.3.15'
    #print sol.compareVersion(ver1, ver2)
    assert sol.compareVersion0(ver1, ver2) == 1, "Not Correct!"
    assert sol.compareVersion(ver1, ver2) == 1, "not Correct!"


