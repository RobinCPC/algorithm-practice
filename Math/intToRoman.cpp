/*
* #: 12
* Title: Integer to Roman
* Description:
* ------
* Given an integer, convert it to a roman numeral.
*
*
* Input is guaranteed to be within the range from 1 to 3999.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Medium
*/
#include <iostream>
#include <vector>
#include <string>
#include <cassert>
using namespace std;


class Solution {
public:
    string intToRoman(int num) {
        vector<string> th {"", "M", "MM", "MMM"};
        vector<string> hu {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        vector<string> te {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        vector<string> di {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string out = th[num/1000] + hu[(num%1000)/100] + te[(num%100)/10] + di[num%10];
        return out;
    }
};


int main(void)
{
    Solution sol = Solution();
    int num = 3989;
    cout << sol.intToRoman(num) << endl;
    assert(sol.intToRoman(num) == "MMMCMXCIX");
    return 0;
}
