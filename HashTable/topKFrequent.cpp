/*
* #: 347
* Title: Top K Frequent Elements
* Description:
* ------
*Given a non-empty array of integers, return the k most frequent elements.
*
*For example,
*Given [1,1,1,2,2,3] and k = 2, return [1,2].
*
*Note:
*
*    You may assume k is always valid, 1 <= k <= number of unique elements.
*    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*
* ------
* Time: O(n*log(n))
* Space: O(n)
* Difficulty: Medium
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <utility>

using namespace std;

// source:	https://discuss.leetcode.com/topic/53674/c-7-lines-hashmap-priority_queue
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for(auto e: nums){
            mp[e]++;
        }
        priority_queue<pair<int, int>> pq;
        for(auto e: mp){
            pq.push(make_pair(e.second, e.first));
        }
        vector<int> out;
        for(int i=0; i<k; ++i){
            out.push_back(pq.top().second);
            pq.pop();
        }
        return out;
    }
};

int main(void)
{
    Solution sol = Solution();
    vector<int> nums = {1,1,1,1,2,2,2,3,3,4,4,4,5,5,5,5,5};
    int k = 2;
    vector<int> result = sol.topKFrequent(nums, k);
    for (auto i:result) cout << i << " ";
    return 0;
}
