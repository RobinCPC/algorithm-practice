/*
* #: 28
* Title: Implement strStr()
* Description:
* ------
* implement strStr().
* 
* Returns the index of the first occurrence of needle in haystack, 
* or -1 if needle is not part of haystack. 
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/
#include <iostream>
#include <string>
using namespace std;

class Solution 
{
    public:
        int strStr(string haystack, string needle)
        {
            if (haystack.empty() && needle.empty())
                return 0;
            if (haystack.empty())
                return -1;
            if (haystack.length() < needle.length())
                return -1;

            for (size_t i = 0; i < haystack.size() - needle.size() + 1; i++)
            {
                size_t j = 0;
                for (; j < needle.size(); j++)
                {
                    if (haystack[i+j] != needle[j])
                        break;
                }
                if ( j == needle.size() )
                    return i;
            }
            return -1;
        }

        int strStr_buildIn(string haystack, string needle) 
        {
            size_t ind = haystack.find(needle);
            if (ind != string::npos)
            {
                return int(ind);
            }
            else
            {
                return -1;
            }
        }
};

int main()
{
    string hay = "helloworld";
    string needle = "owo";
    Solution sol = Solution();
    cout << sol.strStr(hay, needle) << endl;
    return 0;
}
