"""
#: 367
Title: Valid Perfect Square
Description:
------
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

```
Input: 16
Returns: True
```
Example 2:

```
Input: 14
Returns: False
```
------
Time: O(log(n))
Space: O(1)
Difficulty: Medium
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        left, right = 1, num
        while left <= right:
            mid = left + (right - left)/2
            if mid == num / mid and num%mid == 0:
                return True
            elif mid < num / mid:
                left = mid + 1
            else:
                right = mid - 1
        return False


    # Integer Newton
    def isPerfectSquare_Newton(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r > num/r:
            r = (r + num/r) / 2
        return r * r == num



if __name__ == '__main__':
    obj = Solution()
    input = 200
    print obj.isPerfectSquare(input)
    print obj.isPerfectSquare_Newton(input)

