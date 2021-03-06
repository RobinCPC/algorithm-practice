"""
#: 657
Title: Judge Route Circle
Description:
------
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which
means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R
(Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a
circle.

Example 1:
```
Input: "UD"
Output: true
```
Example 2:
```
Input: "LL"
Output: false
```
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


if __name__ == "__main__":
    sol = Solution()
    move = "UUUDDDUDUDLLRRLRLRRLRL"
    print sol.judgeCircle(move)
