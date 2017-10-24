/*
 * #: 692
 * Title: Top K Frequent Words
 * Description:
 * ------
 * Given a non-empty list of words, return the k most frequent elements.
 *
 * Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
 *
 * Example 1:
 *
 * Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * Output: ["i", "love"]
 * Explanation: "i" and "love" are the two most frequent words.
 *     Note that "i" comes before "love" due to a lower alphabetical order.
 *
 * Example 2:
 *
 * Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
 * Output: ["the", "is", "sunny", "day"]
 * Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
 *     with the number of occurrence being 4, 3, 2 and 1 respectively.
 *
 * Note:
 *
 *     You may assume k is always valid, 1 = k = number of unique elements.
 *     Input words contain only lowercase letters.
 *
 * Follow up:
 *
 *     Try to solve it in O(n log k) time and O(n) extra space.
 *
 * ------
 * Time: O(n*log(k))
 * Space: O(n)
 * Difficulty: Medium
 */
#include <iostream>
#include <vector>
#include <unordered_map>    // unordered_map
#include <queue>            // priority_queue
#include <utility>          // pair
#include <algorithm>        // reverse
using namespace std;

class Compare{
  public:
    bool operator() (pair<string, int>& a, pair<string, int>& b) const{
      if (a.second == b.second)
        return (a.first < b.first);
      else
        return (a.second > b.second);
    };
};

class Solution {
  public:
    vector<string> topKFrequent(vector<string>& words, int k) {
      unordered_map<string, int> cnt;
      auto cmp = [] (pair<string, int> a, pair<string, int> b){
        if (a.second == b.second)
          return (a.first < b.first);
        else
          return (a.second > b.second);
      };
      priority_queue< pair<string, int>,
        vector<pair<string, int>>,
        //Compare> pq;
        decltype(cmp)> pq(cmp);
      for (auto& w : words){
        if(cnt.count(w) == 0)
          cnt[w] = 1;
        else
          cnt[w]++;
      }
      for (auto i : cnt){
        pq.push(i);
        if(pq.size() > (size_t)k){
          pq.pop();
        }
      }
      vector<string> res;
      while(!pq.empty()){
        res.push_back(pq.top().first);
        pq.pop();
      }
      reverse(res.begin(), res.end());
      return res;
    }
};

int main(void)
{
  Solution sol = Solution();
  vector<string> words{ "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is" };
  int k = 4;
  vector<string> out = sol.topKFrequent(words, k);
  for(auto i : out){
    cout << i << ' ';
  }
  return 0;
}
