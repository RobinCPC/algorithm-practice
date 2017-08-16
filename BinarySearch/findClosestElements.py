"""
#: 658
Title: Find K Closest Elements
Description:
------
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be
sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
```
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
```
Example 2:
```
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
```
Note:

    The value k is positive and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 104
    Absolute value of elements in the array and x will not exceed 104

------
Time: O(nlgn + klogk)
Space: O(n+k)
Difficulty: Medium
"""
# TODO: use Binary search to find minimum element


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        else:
            shift_ar = sorted([(abs(x-i), i) for i in arr])
        return sorted(i[1] for i in shift_ar[:k])


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k = 3
    x = 5
    print sol.findClosestElements(arr, k, x)
    assert sol.findClosestElements(arr, k, x) == [3, 3, 7], "Not correct!"

