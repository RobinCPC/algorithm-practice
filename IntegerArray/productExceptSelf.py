"""
#: 238
Title: Product of Array Except Self
Description:
------

Given an array of n integers where n > 1, nums, return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does
not count as extra space for the purpose of space complexity analysis.)

------
Time: O(n)
Space: O(1)
Difficulty: Medium
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        [ 1, a[0], a[0]*a[1], a[0]*a[1]*a[2]]
        [a[3]*a[2]*a[1], a[3]*a[2], a[3], 1]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [1] * n
        tmpl, tmpr = 1, 1
        for i in xrange(1, n):
            tmpl *= nums[i-1]
            tmpr *= nums[n-i]
            out[i] *= tmpl
            out[n-i-1] *= tmpr
        return out


if __name__ == '__main__':
    sol = Solution()
    nums = [4,3,2,1,2]
    print sol.productExceptSelf(nums)

