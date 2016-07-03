"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede". 
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        else:
            vow = ['a', 'e', 'i', 'o', 'u']
            lt = list(s)
            left = 0
            right = n - 1
            swapL = False
            swapR = False
            while left <= right:
                if left <= right and lt[left].lower() in vow:
                    swapL = True
                else:
                    left += 1

                if left <= right and lt[right].lower() in vow:
                    swapR = True
                else:
                    right -= 1

                if swapL is True and swapR is True:
                    lt[left], lt[right] = lt[right], lt[left]
                    swapL = swapR = False
                    left += 1
                    right -= 1
            return ''.join(lt)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        else:
            vow = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
            lt = list(s)
            left = 0
            right = n-1
            while left <= right:
                while left <= right and lt[left] not in vow:
                    left += 1
                while left <= right and lt[right] not in vow:
                    right -= 1
                if left >= n or right < 0:
                    break;
                if lt[left] in vow and lt[right] in vow:
                    lt[left], lt[right] = lt[right], lt[left]
                left += 1
                right -= 1
            return ''.join(lt)


if __name__ == '__main__':
    sol = Solution()
    print sol.reverseVowels('oE')
    print sol.reverseVowels('hEllo!')

