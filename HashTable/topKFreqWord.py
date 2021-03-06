"""
#: 692
Title: Top K Frequent Words
Description:
------
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 = k = number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.

------
Time: O(n*log(k))
Space: O(n)
Difficulty: Medium
"""
from collections import Counter
from heapq import heapify, heappush, heappop


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = Counter(words)
        freq = []
        heapify(freq)
        for key, val in cnt.items():
            heappush(freq, (-val, key))
        res = []
        for i in xrange(k):
            res.append(heappop(freq)[1])
        return res


if __name__ == '__main__':
    sol = Solution()
    wds = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print sol.topKFrequent(wds, k)


