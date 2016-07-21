# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# For example,
# Given `1->2->3->3->4->4->5`, return `1->2->5`.
# Given `1->1->1->2->3`, return `2->3`.
#
# time: O(n)
# space: O(1) # constant: need create dummy, curt, and prev (three nodes)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head): # 68ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curt = head
        prev = dummy
        dup = False
        while curt is not None:
            while curt.next is not None and curt.val == curt.next.val:
                dup = True
                curt.next = curt.next.next
            if dup:
                dup = False
                prev.next = curt.next
                curt = prev.next
            else:
                prev = curt
                curt = curt.next
        return dummy.next

if __name__=='__main__':
    L1 = [1,2,2,3,3,4,5]
    n1 = ListNode(L1[0])
    cur_node = n1
    for i in L1[1:]:
        cur_node.next = ListNode(i)
        cur_node = cur_node.next
    sol = Solution()
    print 'before delete duplicate...'
    print n1.val, n1.next.val, n1.next.next.val, n1.next.next.next.val
    n2 = n1.next.next.next.next
    print n2.val, n2.next.val, n2.next.next.val

    res = sol.deleteDuplicates(n1)
    print 'after deleting ...'
    print 'n1='
    print n1.val, n1.next.val, n1.next.next.val
    print 'result='
    print res.val, res.next.val, res.next.next.val

