"""
#: 246
Title: Strobogrammatic Number
Description:
------
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
------
Time: O(n)  # n/2
Space: O(1) # need a fixed hash table
Difficulty: Easy
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strob_dict = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        for i in xrange(len(num)/2 + 1):
            if (num[i] not in strob_dict) or (strob_dict[num[i]] != num[-i-1]):
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print obj.isStrobogrammatic('1960961')
    print obj.isStrobogrammatic('212')


