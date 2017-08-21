"""
#: 102
Title: Binary Tree Level Order Traversal
Description:
------
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).


For example:
Given binary tree `[3,9,20,null,null,15,7]`,
```
    3
   / \
  9  20
    /  \
   15   7
```


return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```
------
Time: O(n)
Space: O(n)
Difficulty: Medium
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        output = []
        que = [root]
        while que:
            subque = []
            subvals = []
            for nd in que:
                subvals.append(nd.val)
                if nd.left:
                    subque.append(nd.left)
                if nd.right:
                    subque.append(nd.right)
            que = subque
            output.append(subvals)
        return output



    def levelOrder_0(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        if root == None:
            return output
        que  = deque()
        que.append((root, 0))
        while (que):
            nd, dep = que.popleft()
            if nd == None:
                continue
            else:
                if len(output) < dep + 1:
                    output.append([nd.val])
                else:
                    output[dep].append(nd.val)
                que.append((nd.left,dep+1))
                que.append((nd.right, dep+1))
        return output


def BFS_insert(node, que_list):
    """
        Use BFS to insert a queue(list) into a binary tree
    """
    from collections import deque
    trav_lt = deque()
    trav_lt.append(node)
    while len(trav_lt) !=0 and len(que_list) != 0:
        if len(que_list) !=0:
            if que_list[0] == 'null':
                que_list.pop(0)
            else:
                trav_lt[0].left = TreeNode(que_list.pop(0))
                trav_lt.append(trav_lt[0].left)

        if len(que_list) !=0:
            if que_list[0] == 'null':
                que_list.pop(0)
            else:
                trav_lt[0].right = TreeNode(que_list.pop(0))
                trav_lt.append(trav_lt[0].right)
        trav_lt.popleft()
    return


if __name__ == '__main__':
    sol = Solution()
    inp_list = [3,9,20,'null','null',15,7]  # [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    print sol.levelOrder_0(root)

