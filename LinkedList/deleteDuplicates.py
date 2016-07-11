"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curt = head
        while curt:
            while curt.next and curt.val == curt.next.val:
                curt.next = curt.next.next
            curt = curt.next
        return head

if __name__ == '__main__':
    L1 = ListNode(1)
    L1.next = ListNode(1)
    L1.next.next = ListNode(2)
    sol = Solution()
    L2 = sol.deleteDuplicates(L1)
    print L1.val
    print L1.next.val
    #print L1.next.next.val


