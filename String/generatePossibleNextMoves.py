"""
#: 296
Title: Flip Game
Description:
------
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:
```
[
  "--++",
  "+--+",
  "++--"
]
```
If there is no valid move, return an empty list [].
------
Time: O(n)
Space: O(n^2)   # worst case, a list to record n possible flip (each w/ n char)
Difficulty: Easy
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        flip = '++'
        out = []
        if not flip in s or len(s) <=1:
            return out
        for i in xrange(len(s) -1):
            if s[i:i+2] == flip:
                out.append(s[0:i] + '--'+ s[i+2:])
        return out


class Solution3(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [ s[0:i] + '--' + s[i+2:] for i in xrange(len(s) - 1) if s[i:i+2] == '++']


if __name__ == '__main__':
    obj = Solution()
    ss = '++++'
    print obj.generatePossibleNextMoves(ss)

