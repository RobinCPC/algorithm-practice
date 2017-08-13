"""
#: 653
Title: Two Sum IV - Input is a BST
Description:
------
Given a Binary Search Tree and a target number, return true if there exist two
elements in the BST such that their sum is equal to the given target.

Example 1:
```
Input:
    5
   / \
  3   6
 / \   \
2   4   7
```
Target = 9

Output: True


Example 2:
```
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
```
Output: False

------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False
        stk, s = [root], set()
        for i in stk:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                stk.append(i.left)
            if i.right:
                stk.append(i.right)
        return False


def BFS_insert(node, que_list):
    """
        Use BFS to insert a queue(list) into a binary tree
    """
    from collections import deque
    trav_lt = deque()
    trav_lt.append(node)
    while len(trav_lt) !=0 and len(que_list) != 0:
        if len(que_list) !=0:
            if que_list[0] == None:
                que_list.pop(0)
            else:
                trav_lt[0].left = TreeNode(que_list.pop(0))
                trav_lt.append(trav_lt[0].left)

        if len(que_list) !=0:
            if que_list[0] == None:
                que_list.pop(0)
            else:
                trav_lt[0].right = TreeNode(que_list.pop(0))
                trav_lt.append(trav_lt[0].right)
        trav_lt.popleft()
    return


if __name__ == '__main__':
    sol = Solution()
    binary_que = [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(binary_que.pop(0))
    BFS_insert(root, binary_que)
    target = 12
    print sol.findTarget(root, target)


