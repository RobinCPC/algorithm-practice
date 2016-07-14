# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        tit = ''
        while (n>0):
            if n%26 != 0:
                tit = chr(64 + n%26) + tit
                n //= 26
            else:
                tit = chr(64 + 26) + tit
                n = n//26 - 1
        return tit

if __name__== '__main__':
    sol = Solution()
    n = 26
    print sol.convertToTitle(n)
    print sol.convertToTitle(27)
    print sol.convertToTitle(78)
    print sol.convertToTitle(199)
    print sol.convertToTitle(2002)
    print sol.convertToTitle(182)


