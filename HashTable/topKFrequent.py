"""
#: 347
Title: Top K Frequent Elements
Description:
------
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given `[1,1,1,2,2,3]` and k = 2, return `[1,2]`.

Note:

    You may assume k is always valid, 1 <= k <= number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

------
Time: O(n*log(n))
Space: O(n)
Difficulty: Medium
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [ key for key, _ in Counter(nums).most_common(k)]


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,1,2,2,2,3,4,4,5,5,5,5,5,5]
    k = 2
    print sol.topKFrequent(nums, k)

