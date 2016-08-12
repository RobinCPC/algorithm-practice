"""
#: 257
Title: Binary Tree Paths
Description:
------
 Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
------
Time: O(n)
Space: O(n)
Difficulty: Easy
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path_list = []
        if root == None:
            return path_list
        path_str = str(root.val)
        self.DFS_helper(root, path_list, path_str)
        return path_list

    def DFS_helper(self, root, path_list, path_str):
        if root.left == None and root.right == None:
            path_list.append(path_str)
            return
        if root.left:
            path_str_left = path_str + '->' + str(root.left.val)
            self.DFS_helper(root.left, path_list, path_str_left)
        if root.right:
            path_str_right = path_str + '->' + str(root.right.val)
            self.DFS_helper(root.right, path_list, path_str_right)
        return

def BFS_insert(node, que_list):
    """Insert a queue(list) into a binary Tree"""
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

#    if len(que_list) != 0:
#        if que_list[0] == None:
#            que_list.pop(0)
#        else:
#            node.left = TreeNode(que_list.pop(0))
#    if len(que_list) != 0:
#        if que_list[0] == None:
#            que_list.pop(0)
#        else:
#            node.right = TreeNode(que_list.pop(0))
#    if len(que_list) == 0:
#        return
#    if node.left != None:
#        BFS_insert(node.left, que_list)
#    if node.right != None:
#        BFS_insert(node.right, que_list)
#    return


if __name__ == '__main__':
    sol = Solution()
    inp_list = [1, 2, 3, None, 5, 6, 7, 8, None, 9, None, 10, 11]   # [1,2,3, None, 5]
    root = TreeNode(inp_list.pop(0))
    BFS_insert(root, inp_list)
    print sol.binaryTreePaths(root)


