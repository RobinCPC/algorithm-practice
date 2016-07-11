/*
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given `1->1->2`, return `1->2`.
Given `1->1->2->3->3`, return `1->2->3`. 
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
using std::cout;
using std::endl;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curt = head;
        while (curt != NULL)
        {
            while (curt->next != NULL && curt->val == curt->next->val)
            {
                curt->next = curt->next->next;
            }
            curt = curt->next;
        }
        return head;
    }
};

int main()
{
    ListNode* L1 = new ListNode(2);
    L1->next = new ListNode(2);
    L1->next->next = new ListNode(3);
    
    Solution sol = Solution();
    ListNode* L2 = sol.deleteDuplicates(L1);
    cout << L1->val << L1->next->val << endl;
    return 0;
}
