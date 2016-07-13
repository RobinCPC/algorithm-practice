"""
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two
lists and sorted in ascending order.

Example:
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        m = None
        head = None
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    if m is None:
                        m = ListNode(l1.val)
                        head = m
                        l1 = l1.next
                    else:
                        curt = ListNode(l1.val)
                        head.next = curt
                        head = head.next
                        l1 = l1.next
                else:
                    if m is None:
                        m = ListNode(l2.val)
                        head = m
                        l2 = l2.next
                    else:
                        curt = ListNode(l2.val)
                        head.next = curt
                        head = head.next
                        l2 = l2.next
            elif l1 is not None and l2 is None:
                if m is None:
                    m = ListNode(l1.val)
                    head = m
                    l1 = l1.next
                else:
                    curt = ListNode(l1.val)
                    head.next = curt
                    head = head.next
                    l1 = l1.next
            elif l1 is None and l2 is not None:
                if m is None:
                    m = ListNode(l2.val)
                    head = m
                    l2 = l2.next
                else:
                    curt = ListNode(l2.val)
                    head.next = curt
                    head = head.next
                    l2 = l2.next
        return m

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(8)
    l1.next.next.next = ListNode(11)
    l1.next.next.next.next = ListNode(15)
    l2 = ListNode(2)

    sol = Solution()
    L = sol.mergeTwoLists(l1, l2)
    print L.val, L.next.val, L.next.next.val, L.next.next.next.val, L.next.next.next.next.val, L.next.next.next.next.next.val
    
