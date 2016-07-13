/*
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two
lists and sorted in ascending order.

Example:
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
*/

#include <stdio.h>
#include <iostream>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
//  12ms
    ListNode* mergeTwoLists_old(ListNode* l1, ListNode* l2) {
        ListNode* m = NULL;  // dummy node
        if( l1==NULL && l2==NULL)
        {
            return l1;
        }
        else if (l1==NULL || l2==NULL)
        {
            return (l1==NULL?l2:l1);
        }
        else
        {
            ListNode* c1 = l1;
            ListNode* c2 = l2;
            if (c1->val <= c2->val)
            {
                m = new ListNode(c1->val);
                c1 = c1->next;
            }else
            {
                m = new ListNode(c2->val);
                c2 = c2->next;
            }
            ListNode* curt = m;
            while( c1!=NULL || c2!=NULL)
            {
                printf("in while");
                if(c1!=NULL && c2!=NULL)
                {
                    if(c1->val <= c2->val )
                    {
                        curt->next = new ListNode(c1->val);
                        c1 = c1->next;
                        curt = curt->next;
                    }else
                    {
                        curt->next = new ListNode(c2->val);
                        c2 = c2->next;
                        curt = curt->next;
                    }
                }else
                {
                    if(c1!=NULL)
                    {
                        curt->next = c1;
                        c1 = NULL;
                    }
                    else
                    {
                        curt->next = c2;
                        c2 = NULL;
                    }
                }
            }
        }
        return m;
    }
// 13ms
    ListNode* mergeTwoLists2(ListNode* l1, ListNode* l2) {
        ListNode* m = NULL;  // dummy node
        if( l1==NULL && l2==NULL)
        {
            return l1;
        }
        else if (l1==NULL || l2==NULL)
        {
            return (l1==NULL?l2:l1);
        }
        else
        {
            m = new ListNode(0);
            ListNode* curt = m;
            while( l1!=NULL || l2!=NULL)
            {
                if(l1!=NULL && l2!=NULL)
                {
                    if(l1->val <= l2->val )
                    {
                        curt->next = l1;
                        l1 = l1->next;
                        curt = curt->next;
                    }else
                    {
                        curt->next = l2;
                        l2 = l2->next;
                        curt = curt->next;
                    }
                }else
                {
                    if(l1!=NULL)
                    {
                        curt->next = l1;
                        l1 = NULL;
                    }
                    else
                    {
                        curt->next = l2;
                        l2 = NULL;
                    }
                }
            }
        }
        return (m==NULL)?(m):(m->next);
    }
// solution from book  12ms
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(0);
        ListNode *lastNode = dummy;
        while ((NULL != l1) && (NULL != l2)) {
            if (l1->val < l2->val) {
                lastNode->next = l1;
                l1 = l1->next;
            } else {
                lastNode->next = l2;
                l2 = l2->next;
            }

            lastNode = lastNode->next;
        }

        // do not forget this line!
        lastNode->next =  (NULL != l1) ? l1 : l2;

        return dummy->next;
    }

};

int main()
{
    ListNode* L1 = new ListNode(1);
    L1->next = new ListNode(3);
    L1->next->next = new ListNode(5);

    ListNode* L2 = new ListNode(2);
    L2->next = new ListNode(4);
    L2->next->next = new ListNode(6);

    Solution sol = Solution();
    ListNode* LL = sol.mergeTwoLists(L1, L2);
    std::cout << LL->val << LL->next->val << LL->next->next->val << LL->next->next->next->val << '\n';
    return 0;
}
