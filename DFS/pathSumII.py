"""
#: 113
Title: Path Sum II
Description:
------
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```
return
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```
------
Time: O(n)
Space: O(h)
Difficulty: Medium
"""

class TreeNode(object):
    """Definition of a binary tree node"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path_list = []
        path = []
        if root is None:
            return path_list
        path.append(root.val)
        self.DFS_helper(root, sum, path, path_list)
        return path_list

    def DFS_helper(self, node, target, path, path_list):
        if node.left is None and node.right is None:
            if sum(path) == target:
                path_list.append(path)
            return
        if node.left:
            path_left = [item for item in path]
            path_left.append(node.left.val)
            self.DFS_helper(node.left, target, path_left, path_list)
        if node.right:
            path_right = [item for item in path]
            path_right.append(node.right.val)
            self.DFS_helper(node.right, target, path_right, path_list)
        return


def BFS_insert(root, que_list):
    """
        Use BFS to insert a list into binary tree
    """
    from collections import deque
    que_list.reverse()
    trav_lt = deque()
    trav_lt.append(root)
    while len(trav_lt) != 0 and len(que_list) != 0:
        if len(que_list) != 0:
            if que_list[-1] is None:
                que_list.pop()
            else:
                trav_lt[0].left = TreeNode(que_list.pop())
                trav_lt.append(trav_lt[0].left)
        if len(que_list) != 0:
            if que_list[-1] is None:
                que_list.pop()
            else:
                trav_lt[0].right = TreeNode(que_list.pop())
                trav_lt.append(trav_lt[0].right)
        trav_lt.popleft()
    return

if __name__ == '__main__':
    sol = Solution()
    inp_list = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    target = 22
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    print sol.pathSum(root, target)

