"""
#: 128
Title: Longest Consecutive Sequence
Description:
------
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given `[100, 4, 200, 1, 3, 2]`,
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.

Your algorithm should run in O(n) complexity.
------
Time: O(n)
Space: O(n)
Difficulty: Hard
"""
# Source: https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak/2
# Use set (hash table can do O(1) lookup) to record all unique elements, and
# find the first continues number, then find through the last continues number.
# Final, check if the longest consecutive sequence.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = set(nums)
        result = 0
        for x in record:
            if (x-1) not in record:
                y = x + 1
                while y in record:
                    y += 1
                result = max(result, y-x)
        return result


if __name__ == '__main__':
    nums = [100, 1, 200, 3, 2, 4]
    sol = Solution()
    print sol.longestConsecutive(nums)

