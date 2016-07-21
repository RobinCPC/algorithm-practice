/* #: 242
* Given two strings s and t, write a function to determine if t is an anagram of s.
* 
* For example,
* s = "anagram", t = "nagaram", return true.
* s = "rat", t = "car", return false.
* 
* Note:
* You may assume the string contains only lowercase alphabets.
* 
* Follow up:
* What if the inputs contain unicode characters? How would you adapt your solution to such case?
* 
* time: O(n)
* space: O(1)
* 
*/
#include <iostream>
#include <string>
using namespace std;

class Solution 
{
public:
    bool isAnagram(string s, string t) 
    {
        if (s.length() != t.length())
            return false;
        int cnt_char[256] = {0};
        for (int i=0; i < s.size(); ++i)
        {
            cnt_char[int(s.at(i))] +=1;
            cnt_char[int(t.at(i))] -=1;
        }
        for (int j=0; j < 256; ++j)
        {
            if (cnt_char[j] != 0)
                return false;
        }
        return true;
    }

};

int main()
{
    Solution sol = Solution();
    cout << sol.isAnagram("hel!lo","olleh ") << endl;
    return 0;
}
