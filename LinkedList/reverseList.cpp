/*
* #: 206
* Title: Reversed Linked List
* Description:
* ------
* Reverse a singly linked list.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/
#include <iostream>
#include <vector>

// Definition of singly linked list
struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution{
public:
    ListNode* reverseList(ListNode* head){
        ListNode* prev{};
        ListNode* mid{head};
        ListNode* next;

        while(mid){
            next = mid->next;
            mid->next = prev;
            prev = mid;
            mid = next;
        }
        return prev;
    }
};

int main(void)
{
    std::vector<int> L1 = {1,3,5,7,8,9};
    ListNode n1 = ListNode(L1[0]);

    ListNode* curt = &n1;

    for (unsigned int i=1; i < L1.size(); ++i){
        curt->next = new ListNode(L1[i]);
        curt = curt->next;
    }
    std::cout << "before reverse:\n";
    curt =&n1;
    while (curt){
        std::cout << curt->val << ", ";
        curt = curt->next;
    }
    Solution sol = Solution();
    ListNode* result = sol.reverseList(&n1);
    std::cout << "\n after reverse: \n";
    curt = result;
    while (curt){
        std::cout << curt->val << ", ";
        curt = curt->next;
    }
    std::cout << "\n";
    return 0;
}
