"""
#: 47
Title: Permution II
Description:
------
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

 For example,
 [1,1,2] have the following unique permutations:
 ```
 [
   [1,1,2],
   [1,2,1],
   [2,1,1]
 ]
 ```
------
Time: O(n*n!)
Space: O(n)
Difficulty: Medium
Note: there are n! permutations and it requires O(n) to find a permutation.
"""
#TODO: Check Complexity


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        pre_list = [[]]
        for val in nums:
            tmp_list = []
            for lst in pre_list:
                n_len = len(lst)
                for n in xrange(n_len+1):
                    tmp = lst[:n]+[val]+lst[n:]
                    tmp_list.append(tmp)
                    if n < n_len and lst[n] == val:
                        break
            pre_list = tmp_list
        pre_list.sort()
        return pre_list


if __name__ == '__main__':
    obj = Solution()
    num_lst = [1,2,1]
    print obj.permuteUnique(num_lst)

