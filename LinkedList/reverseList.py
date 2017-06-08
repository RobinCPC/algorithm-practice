"""
#: 206
Title: Reverse Linked List
Description:
------
Reverse a singly linked list
------
Time: O(n)
Space: O(1)
Difficulty: Easy
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        next = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


if __name__ == '__main__':
    L1 = [1,3,5,8,7,9,12]
    n1 = ListNode(L1[0])
    curt = n1
    for i in L1[1:]:
        curt.next = ListNode(i)
        curt = curt.next
    sol = Solution()
    print 'before reverse linked list:'
    curt = n1
    tmp = []
    while(curt):
        tmp.append(curt.val)
        curt = curt.next
    print tmp

    res = sol.reverseList(n1)
    print 'after reverse:'
    curt = res
    tmp2 = []
    while(curt):
        tmp2.append(curt.val)
        curt = curt.next
    print tmp2


