"""
#: 189
Title: Rotate Array
Description:
------
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Could you do it in-place with O(1) extra space?
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""
import resource  # check memory usage (may not use the right way)
# TODO: learn how to check space usage

class Solution(object):
    """
    :type nums: List[int]
    :type offset: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, offset):      # 76 ms
        if offset != 0:
            offset %= len(nums)
            nums[::] = nums[-offset:] + nums[:-offset]  # (Space O(1)?)

    def rotate2(self, nums, offset):     # recursive way will fail if offset too big
        if offset!=0:                    # too many recursive layer
            if offset > len(nums):
                offset %= len(nums)
            offset -= 1
            p_num = nums.pop()
            nums.insert(0, p_num)
            self.rotate2(nums, offset)

class Solution2(object):
    def rotate(self, nums, offset):      # 88 ms
        if offset!=0 and len(nums)>1 :
            offset, end = offset%len(nums), len(nums)-1
            self.reverse(nums, 0, end - offset)
            self.reverse(nums, end - offset + 1, end)
            self.reverse(nums, 0, end)
        print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    sol = Solution2()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
    print 'nums = ', nums
    print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;

