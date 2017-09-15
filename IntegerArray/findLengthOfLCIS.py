"""
#: 674
Title: Longest Continuous Increasing Subsequence
Description:
------
 Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
```
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
```

Example 2:
```
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
```

Note: Length of the array will not exceed 10,000.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_len = 1
        begin = 0
        for i in xrange(1, len(nums)):
            if nums[i] > nums [i-1]:
                tmp = i - begin + 1
                max_len = max(max_len, tmp)
            else: # < or  ==
                begin = i
        return max_len


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 3, 5, 4, 7]
    print sol.findLengthOfLCIS(arr)

