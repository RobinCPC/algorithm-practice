/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
*/

#include <iostream>
#include <string>
using std::string;
using std::cout;

class Solution {
public:
    string convertToTitle(int n) {
        string c = string("");
        while(n>0)
        {
            if( n%26 !=0)
            {
                c = (char)(64 + n%26) + c;
                n /= 26;
            }
            else
            {
                c = (char)(64+26) + c;
                n = n/26 - 1;
            }
            
        }
        return c;
    }
};

int main()
{
    Solution sol = Solution();
    int n = 26;
    cout << sol.convertToTitle(n) << '\n';
    cout << sol.convertToTitle(27) << '\n';
    cout << sol.convertToTitle(78) << '\n';
    cout << sol.convertToTitle(199) << '\n';
    cout << sol.convertToTitle(2002) << '\n';
    cout << sol.convertToTitle(182) << '\n';
    
    return 0;
}
