"""
#: 645
Title: Set Mismatch
Description:
------

The set S originally contains numbers from 1 to n. But unfortunately, due to the
data error, one of the numbers in the set got duplicated to another number in the
set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number
that is missing. Return them in the form of an array.

Example 1:
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

Note:

The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ind = [0] * (len(nums) + 1)     # a hash table to record used number
        rep = 0     # record repeated number
        for e in nums:
            if ind[e] != 1:
                ind[e] = 1
            else:
                rep = e
                break
        org = (1 + len(nums)) * len(nums) / 2   # original sum if no errorj
        mis = org - ( sum(nums) - rep)
        return [rep, mis]


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2,4]
    assert (sol.findErrorNums(nums) == [2,3]), "not correct"
    print sol.findErrorNums(nums)
