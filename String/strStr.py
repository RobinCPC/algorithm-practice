"""
 Implement strStr().

Returns the index of the first occurrence of needle in haystack, or 
-1 if needle is not part of haystack. 

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        if len(haystack) < len(needle):
            return -1
        
        for i in xrange(len(haystack) - len(needle) + 1 ):
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else: # special else method : means 'no break'
            # if j == len(needle)-1:
                return i
        return -1
        #return haystack.find(needle)


if __name__ == '__main__':
    sol = Solution()
    print sol.strStr('helloworld','owo')

