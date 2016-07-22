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
#include <iostream>
#include <vector>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


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

int main(int argc, char* argv[])
{
    std::vector<int> L1 = {1,1,2,3,3,4,5,5};
    ListNode n1 = ListNode(L1[0]);
    //ListNode* p2 = new ListNode(L1[0]);
    ListNode* curt = &n1;
    //ListNode* curt = p2;
    for(int i=1; i< L1.size(); ++i)
    {
        curt->next = new ListNode(L1[i]);   // will become dangling ptr?
        curt = curt->next;
    }
    std::cout << "before delete duplicate...\n";
    curt = &n1;
    for(int i=0; i<L1.size(); ++i)
    {
        std::cout << curt->val << ", ";
        curt = curt->next;
    }
    Solution sol = Solution();
    ListNode* result = sol.deleteDuplicates(&n1);
    curt = &n1;
    std::cout << "\n after, n1=..." << std::endl;
    while (curt != NULL)
    {
        std::cout << curt->val << ", ";
        curt = curt->next;
    }
    std::cout << "\n then, result=..." << std::endl;
    curt = result;
    while (curt != NULL)
    {
        std::cout << curt->val << ", ";
        curt = curt->next;
    }
    std::cout << '\n';

    return 0;
}
