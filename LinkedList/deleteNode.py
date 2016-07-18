# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
# with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
#
# time: O(1)
# space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
   def deleteNode2(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curt = node
        prev = None
        while curt.next is not None:
            curt.val = curt.next.val
            prev = curt
            curt = curt.next
        if prev is not None:
            prev.next = None
        return

   def deleteNode1(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curt = node
        while curt.next is not None:
            curt.val = curt.next.val
            if curt.next.next is None:
                curt.next = None
                break
            curt = curt.next
        return

   def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    sol = Solution()
    sol.deleteNode(n1)
    print n1.val, n1.next.val, n1.next.next.val
    try:
        print n1.next.next.next.val
    except:
        print 'None Type!'
        pass


