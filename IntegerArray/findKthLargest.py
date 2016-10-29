"""
#: 215
Title: Kth Largest Element in an Array
Description:
------
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.
------
Time: O(nlog(n))
Space: O(1)
Difficulty: Medium
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

# should build quicksort DIY

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,6,5,4]
    k = 2
    print sol.findKthLargest(nums, k)

