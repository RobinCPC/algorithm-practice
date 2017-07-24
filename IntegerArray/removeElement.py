"""
#: 27
Title: Remove Element
Description:
------
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = `[3,2,2,3]`, val = `3`

Your function should return length = 2, with the first two elements of nums being 2.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        h = 0
        t = nums.__len__() - 1
        while h <= t:
            if nums[h] == val:
                nums[h] = nums[t]
                t -= 1
            else:
                h += 1
        return t + 1


if __name__ == '__main__':
    Sol = Solution()
    nums = [4,1,2,3,5]
    val = 4
    leng = Sol.removeElement(nums, val)
    print( nums[:leng])
