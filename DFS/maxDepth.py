"""
#: 104
Title: Maximum Depth of Binary Tree
Description:
------
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

# Definition of binary tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDept(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDept = 0
        if root == None:
            return maxDept
        elif root.left == None and root.right == None:
            return maxDept + 1
        if root.left != None:
            maxDept = self.DFShelper(root.left, 1, maxDept)
        if root.right != None:
            maxDept = self.DFShelper(root.right, 1, maxDept)
        return maxDept


    def DFShelper(self,node, cur_dep, max_dep):
        cur_dep += 1
        if node.left == None and node.right == None:
            if cur_dep > max_dep:
                return cur_dep
        if node.left != None:
            max_dep = self.DFShelper(node.left, cur_dep, max_dep)
        if node.right != None:
            max_dep = self.DFShelper(node.right, cur_dep, max_dep)
        return max_dep


def BFS_insert(node, que_list):
    """
        Use BFS to insert a queue(list) into a binary tree
    """
    from collections import deque
    trav_lt = deque()
    trav_lt.append(node)
    while len(trav_lt) != 0 and len(que_list) != 0:
        if len(que_list) != 0:
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
    inp_list = [1,2,3,4,5,6,7]
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    print sol.maxDept(root)


