/*
* #: 246
* Title: Strobogrammatic Number
* Description:
* ------
A strobogrammatic number is a number that looks the same when rotated 180 
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is 
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty:  Easy
*/

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char> strob_dict({{'6','9'}, {'9','6'}, {'0','0'} , {'1','1'}, {'8','8'}});
        for(int i = 0; i < int(num.length()/2)+1; ++i)
        {
            if (strob_dict[num[i]])
            {
                if( strob_dict[num[i]] != num.at(num.length()-i -1))
                {
                    return false;
                }
            }else{
                return false;
            }
        }
        return true;
    }
};

int main(void)
{
    Solution obj = Solution();
    string num("8160918");
    bool val =obj.isStrobogrammatic(num);
    cout << val << '\n';
    return 0;
}
