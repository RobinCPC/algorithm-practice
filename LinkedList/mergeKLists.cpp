/*
* #: 23
* Title: Merge K Sorted Lists
* Description:
* ------
* Merge k sorted linked lists and return it as one sorted list. 
* Analyze and describe its complexity.
* ------
* Time: O(n*k*log(n)  // n is # of list and k is average element in each listnode
* Space: O( 1/2 *n*k*log(n))
* Difficulty:  Easy
*/
// Source: https://discuss.leetcode.com/topic/6882/sharing-my-straightforward-c-solution-without-data-structure-other-than-vector 
// TODO: Check space

#include <iostream>
#include <vector>
using std::vector;
using std::cout;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()) return nullptr;
        int len = lists.size();
        while(len > 1){
            for (int i = 0; i < len/2; ++i){
                lists[i] = mergeTwoLists(lists[i], lists[len - 1 -i]);
            }
            len = (len + 1) / 2;
        }
        return lists.front();
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
        if(nullptr == l1)
            return l2;
        else if (nullptr == l2)
            return l1;
        if (l1->val <= l2->val){
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};


int main(void)
{
    
    ListNode* L1 = new ListNode(1);
    L1->next = new ListNode(3);
    L1->next->next = new ListNode(5);

    ListNode* L2 = new ListNode(2);
    L2->next = new ListNode(4);
    L2->next->next = new ListNode(6);

    ListNode* L3 = new ListNode(0);
    L3->next = new ListNode(7);
    L3->next->next = new ListNode(9);
    
    vector<ListNode*> Lists;
    Lists.push_back(L1);
    Lists.push_back(L2);
    Lists.push_back(L3);

    Solution sol = Solution();
    ListNode* LL = sol.mergeKLists(Lists);

    ListNode* head = LL;

    while(head){
        cout << head->val << ", ";
        head = head->next;
    }

    return 0;
}
