"""
#: 112
Title: Path Sum
Description:
------
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = False
        if root == None:
            return result
        total = root.val
        if root.left == None and root.right == None:
            if total == sum:
                return True
            else:
                return False
        if root.left != None and result != True:
            left_tot = total
            result = self.DFS_helper(root.left, left_tot, sum)
        if root.right != None and result != True:
            right_tot = total
            result = self.DFS_helper(root.right, right_tot, sum)
        return result


    def DFS_helper(self, node, total, sum):
        total += node.val
        if node.left == None and node.right == None:
            if total == sum:
                return True
            else:
                return False
        result = False
        if node.left != None:
            left_tot = total
            result = self.DFS_helper(node.left, left_tot, sum)
        if node.right != None and result != True:
            right_tot = total
            result = self.DFS_helper(node.right, right_tot, sum)
        return result


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
    inp_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]   # [1,2,3, None, 5]
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    print sol.hasPathSum(root, 22)

