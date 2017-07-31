"""
#: 217
Title: Contains Duplicate
Description:
------

Given an array of integers, find if the array contains any duplicates. Your
function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = {}  # rrecord what already have
        for e in nums:
            if e in hash_table:
                return True
            else:
                hash_table[e] = 1
        return False

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,6,8,7,9,3,10]
    print sol.containsDuplicate(nums)
    print sol.containsDuplicate1(nums)

