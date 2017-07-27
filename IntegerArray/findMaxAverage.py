"""
#: 634
Title: Maximum Average Subarray I
Description:
------

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.


Example 1:
```
    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
```


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_val = float("-inf")  # a -inf number
        cum = sum(nums[:k])
        if cum >= max_val:
            max_val = cum
        for i in xrange(k, len(nums)):
            cum += nums[i]
            cum -= nums[i-k]
            if cum >= max_val:
                max_val = cum
        return float(max_val) / k


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert(sol.findMaxAverage(nums, k) == 12.75), "not correct!"
    print sol.findMaxAverage(nums, k)
