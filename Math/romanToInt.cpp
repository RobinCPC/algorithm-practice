/*
* #: 13
* Title: Roman to Integer
* Description:
* ------
* Given a roman numeral, convert it to an integer.
*
* Input is guaranteed to be within the range from 1 to 3999.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Easy
*/
#include <iostream>
#include <unordered_map>
#include <string>
#include <cassert>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> r2i = { {'I', 1},
                                        {'V', 5},
                                        {'X', 10},
                                        {'L', 50},
                                        {'C', 100},
                                        {'D', 500},
                                        {'M', 1000} };
        int out = 0;
        for (size_t i=0; i < s.length()-1; ++i){
            if(r2i[s[i]] < r2i[s[i+1]]){
                out -= r2i[s[i]];
            }else{
                out += r2i[s[i]];
            }
        }
        out += r2i[s.back()];
        return out;
    }
};


int main(void)
{
    Solution sol = Solution();
    string romstr = "MMMCMXCIX";
    cout << sol.romanToInt(romstr) << endl;
    assert(sol.romanToInt(romstr) == 3999);
    return 0;
}

