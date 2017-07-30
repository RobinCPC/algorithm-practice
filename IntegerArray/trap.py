"""
#: 42
Title: Trapping Rain Water
Description:
------

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.


For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
for contributing this image!

------
Time: O(n)
Space: O(1)
Difficulty: Hard
"""

class Solution(object):
    def trap(self, height):
        """
        find the index with max_height
        then, loop from left till hei_index and fill water depend on the local
        height of left. Do the same from right again.
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        h_ind = height.index(max(height))   # find the index with max_height

        result = 0  # store how many rain will trap
        max_lf = 0
        for e in height[:h_ind]:
            if e > max_lf:
                max_lf = e
            elif e < max_lf:
                result += max_lf -e

        max_rt = 0
        for e in height[h_ind:][::-1]:
            if e > max_rt:
                max_rt = e
            elif e < max_rt:
                result += max_rt - e
        return result

if __name__ == '__main__':
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print sol.trap(height)

