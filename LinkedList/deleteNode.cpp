/* 
 * Write a function to delete a node (except the tail) in a singly linked list,
 * given only access to that node.
 * 
 * Supposed the linked list is `1 -> 2 -> 3 -> 4` and you are given the third node with value 3,
 * the linked list should become `1 -> 2 -> 4` after calling your function.
 *
 * time: O(1)  
 * space: O(1)
*/
#include <iostream>
using std::cout;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void deleteNode2(ListNode* node) { // 17ms
        ListNode* curt = node;
        while(curt->next != NULL)
        {
            curt->val = curt->next->val;
            if(curt->next->next == NULL)
            {
                curt->next == NULL;
                break;
            }
            curt = curt->next;
        }
        return;
    }

    void deleteNode1(ListNode* node) {
        ListNode* curt = node;
        curt->val = curt->next->val;
        curt->next = curt->next->next;   
        return;
    }
    
    void deleteNode(ListNode* node) { // 16ms
        auto next = node->next;
        // *node = *(node->next);
        *node = *next;
        delete next;
    }
};

int main()
{
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    ListNode* n4 = new ListNode(4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    Solution sol = Solution();
    sol.deleteNode(n2);
    cout << n1->val<< n1->next->val << n1->next->next->val << '\n';    
    return 0;
}

