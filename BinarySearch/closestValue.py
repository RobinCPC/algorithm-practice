"""
#: 270
Title: Closest Binary Search Tree Value
Description:
------
Given a non-empty binary search tree and a target value, find the value in
the BST that is closest to the target.

Note:
    * Given target value is a floating point.
    * You are guaranteed to have only one unique value in the BST that is
      closest to the target.
------
Time: O(log(n))
Space: O(1)
Difficulty: Easy
"""


# Definition for a binary tree Node.
class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root.left == None and root.right == None:
            return root.val
        cl_val = root.val
        if root.left != None and cl_val > target:
            cl_val = self.BSThelper(root.left, target, cl_val)
        elif root.right != None and cl_val <= target:
            cl_val = self.BSThelper(root.right, target, cl_val)
        return cl_val


    def BSThelper(self, node, target, cl_val):
        if abs(target - node.val) < abs(target - cl_val):
            cl_val = node.val
        if node.left != None and node.val > target:
            cl_val = self.BSThelper(node.left, target, cl_val)
        elif node.right != None and node.val <= target:
            cl_val = self.BSThelper(node.right, target, cl_val)
        return cl_val


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
    obj = Solution()
    inp_list = [5, 2, 8, 0, 3, 6, 9]
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    target = 7
    print obj.closestValue(root, target)



