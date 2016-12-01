/*
* #: 266
* Title: Palindrome Permutation
* Description:
* ------
* Given a string, determine if a permutation of the string could form a palindrome.
*
* For example,
* ```
* "code" -> False, "aab" -> True, "carerac" -> True."
* ```
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/
#include <iostream>
#include <unordered_map>
using namespace std;


class Solution
{
public:
    bool canPermutePalindrome(string s)
    {
        unordered_map <char, int> table;
        int n_odd_cnt = 0;
        for (char c : s)
        {
            ++table[c];
            (table[c] % 2 == 0) ? --n_odd_cnt : ++n_odd_cnt;
        }
        return n_odd_cnt <= 1;
    }
};

int main(void)
{
    Solution obj  = Solution();
    string ss = "code";    //"aab";
    if (obj.canPermutePalindrome(ss))
        cout << "True\n";
    else
        cout << "False\n";
    return 0;
}
