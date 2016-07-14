/*
* Given a column title as appear in an Excel sheet, return its corresponding column number.
* 
* For example:
* 
*     A -> 1
*     B -> 2
*     C -> 3
*     ...
*     Z -> 26
*     AA -> 27
*     AB -> 28
* 
* time: O(n)
* space: O(1) 
*/

#include <string>
#include <iostream>
#include <cmath>

using std::string;
using std::cout;

class Solution {
public:
    int titleToNumber2(string s) { // 12ms
        int num = 0;
        size_t digit = s.size() - 1;
        for (int i=0 ; digit != string::npos; --digit, ++i)
        {
            num += pow(26, digit) * ( (int)s[i] - 64);
        }
        return num;
    }

    int titleToNumber(string s) { // 8ms (without pow)
        int num = 0;
        size_t digit = s.size() - 1;
        for (int i=0 ; digit != string::npos; --digit, ++i)
        {
            num = num * 26 + ( (int)s[i] - 64);
        }
        return num;
    }
};

int main()
{
    string s = string("AA");
    Solution sol = Solution();
    cout << sol.titleToNumber(s) << '\n';
    cout << sol.titleToNumber("GQ") << '\n';
    cout << sol.titleToNumber("BXZ") << '\n';
    cout << sol.titleToNumber("Z") << '\n';
    return 0;
}
