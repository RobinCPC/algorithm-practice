'''
#: 1
Title: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

------

Time: O(n)
Space:O(n)  # need extra space for hash table
Difficulty: Easy
'''

class Solution(object):
    def twoSum_list(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            rem = target - nums[i]
            try:
                return [i, nums[i+1:].index(rem)+(i+1)]
            except:
                pass
        return None

    def twoSum_fail(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for ind in xrange(len(nums)):
            num_dict[ ind ] = nums[ind]
        for k,v in num_dict:
            rem = target - v
            if rem in num_dict.values():
                #import pdb
                #pdb.set_trace()
                return [i, num_dict[rem]]
        return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for ind, val in enumerate(nums):
            if target - val in nums_hash:
                return [ nums_hash[target-val], ind ]
            nums_hash[val] = ind
        return [-1, -1]

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([0, 4, 3, 0],0)

