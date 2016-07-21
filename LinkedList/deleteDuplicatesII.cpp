/*
* Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
*
* For example,
* Given 1->2->3->3->4->4->5, return 1->2->5.
* Given 1->1->1->2->3, return 2->3.
*
* time: O(n)
* space: O(1)
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy = ListNode(0);
        dummy.next = head;
        ListNode* curt = head;
        ListNode* prev = &dummy;
        bool dup = false;
        while(curt != NULL)
        {
            while(curt->next != NULL && curt->val == curt->next->val)
            {
                dup = true;
                curt->next = curt->next->next;
            }
            if(dup)
            {
                dup = false;
                prev->next = curt->next;
                curt = prev->next;
            }
            else
            {
                prev = curt;
                curt = curt->next;
            }
        }
        return dummy.next;
    }
};
