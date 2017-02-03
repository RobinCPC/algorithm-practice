"""
#: 23
Title: Merge k Sorted Lists
Description:
------
Merge k sorted Lists and return it as one sorted list. Analyzed
and describe its complexity.
------
Time: O(n*k*log(n)  // n is # of list and k is average elements in each listnode
Space: O(1/2 n*k*log(n))
Difficulty: Hard
"""
# TODO: check space

# Definition for singly-linked List.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        lens = len(lists)
        while lens > 1:
            for i in xrange(lens/2):
                lists[i] = self.mergeTwoLists(lists[i], lists[lens -1 -i])
            lens = (lens + 1) / 2
        #while len(lists) > 1:
        #    lists.append(self.mergeTwoLists(lists[0], lists[1]))
        #    lists = lists[2:]
        return lists[0]


    def mergeKLists_TLE(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        outlist = lists[0]
        for j in lists[1:]:
            outlist = self.mergeTwoLists(outlist, j)
        return outlist



    def mergeTwoLists(self, l1, l2):
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

# Source: https://discuss.leetcode.com/topic/23140/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
# TODO: check Time Complexity
class Solution2(object):
    def mergeKLists(self, lists):
        """
        with heapq and avoid changing heap size
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next


def build_listNode(array):
    """
    :type array: list
    :rtype : ListNode
    """
    if len(array) == 0:
        return None
    ln = ListNode(array[0])
    cur = ln
    for i in array[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return ln


if __name__ == '__main__':
    klist = [[1, 5, 9], [2, 6, 8],[4, 7, 12]]
    #klist = [[],[4, 7, 12]]
    kListNode = [build_listNode(i) for i in klist]
    sol = Solution2()
    outlist = sol.mergeKLists(kListNode)
    cur = outlist
    while cur:
        print cur.val
        cur = cur.next



