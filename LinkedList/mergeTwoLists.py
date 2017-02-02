"""
#: 21
Title: Merge Two Sorted Lists
Description:
------
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two
lists and sorted in ascending order.

Example:
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
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


# Source: https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place
class Solution2(object):
    # iteratively
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # recursively
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2

    # in-place, iteratively
    def mergeTwoLists3(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next



if __name__ == '__main__':
    l1_element = [1, 3, 8, 11, 15]
    l1 = ListNode(l1_element[0])
    node = l1
    for i in l1_element[1:]:
        node.next = ListNode(i)
        node = node.next

    l2_element = [2, 7, 10, 13]
    l2 = ListNode(l2_element[0])
    node = l2
    for i in l2_element[1:]:
        node.next = ListNode(i)
        node = node.next

    #sol = Solution()
    #L = sol.mergeTwoLists(l1, l2)
    #print L.val, L.next.val, L.next.next.val, L.next.next.next.val, L.next.next.next.next.val, L.next.next.next.next.next.val

    sol2 = Solution2()
    L2 = sol2.mergeTwoLists3(l1,l2)
    cur2 = L2
    while cur2:
        print cur2.val
        cur2 = cur2.next

