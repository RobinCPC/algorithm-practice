"""
#: 53
Title: Maximum maxSubArray
Description:
------
 Find the contiguous subarray within an array (containing at least one number)
 which has the largest sum.

 For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] has the largest sum = 6.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        curSum = maxSum = nums[0]
        for i in xrange(1, len(nums)):
            curSum = max(nums[i], curSum+nums[i])
            maxSum = max(curSum, maxSum)
        return maxSum


    def maxSubArray_dp0(self, nums):
        """
        DP but scan all (that make it slow)
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        dp_arr = []
        out = max(nums)
        out_list = []
        dp_arr.append(nums)
        i = 1
        while i < n:
            j = 0
            arr = []
            while j + i < n:
                tmp = dp_arr[i - 1][j] + dp_arr[0][j + i]
                if tmp > out:
                    out = tmp
                    out_list = nums[j:(i + j + 1)]
                arr.append(tmp)
                j += 1
            dp_arr.append(arr)
            i += 1
        return out



    def maxSubArray_brute(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force
        out = []
        n_nums = len(nums)
        if n_nums == 0:
            return out
        elif n_nums == 1:
            return nums
        else:
            max_val = max(nums)
            for i in xrange(n_nums+1):
                for j in xrange(i+2, n_nums+1):
                    #print nums[i:j]
                    max_val = max(max_val, sum(nums[i:j]))
                    #out = nums[i:j] if sum(nums[i:j]) > max_val else out
            return max_val
            #return out if out else [max_val]


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert sol.maxSubArray(nums)==6, "Not currect!"
