"""
#: 400
Title: Nth Digit
Description:
------
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
```
Input:
3

Output:
3
```

Example 2:
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, 
which is part of the number 10.
```
------
Time: O(log(n))
Space: O(1)
Difficulty: Easy
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, digit, step = 1, 1, 9
        while n > step * digit:
            n = n - (step*digit)
            digit +=1
            step *= 10
            start *=10
        num = start + (n-1)/digit
        sub_digit = (n-1)%digit
        n_digit = int(str(num)[sub_digit])
        return n_digit


if __name__ == '__main__':
    obj = Solution()
    print obj.findNthDigit(11)
    print obj.findNthDigit(12)
    print obj.findNthDigit(13)
