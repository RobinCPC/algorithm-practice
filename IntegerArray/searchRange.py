"""
#: 34
Title: Search Range
Description:
------
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return `[-1, -1]`.

For example,
Given `[5, 7, 7, 8, 8, 10]` and target value 8,
return `[3, 4]`.
------
Time: O(n)
Space: O(1)
Difficulty: Medium
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range = [-1,-1]
        if target in nums:
            start = nums.index(target)
            end = nums[::-1].index(target)
            end =  len(nums)-end - 1
            return [start, end]
        return range



if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 9, 10]
    target = 7
    result = sol.searchRange(nums, target)
    print 'Given\n', nums
    print 'Target', target
    print 'Return ', result
