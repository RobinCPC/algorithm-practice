/*
implement strStr().

Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack. 
*/
#include <iostream>
#include <string>
using namespace std;

class Solution 
{
    public:
        int strStr(string haystack, string needle) 
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
