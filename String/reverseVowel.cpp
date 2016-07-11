/*
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede". 
*/

#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

class Solution {
public:
    string reverseVowels(string s) 
    {
        size_t n = s.length();
        if (n <= 1)
        {
            return s;
        }
        else
        {
            string vow = "aeiouAEIOU";
            int left = 0;
            int right = n-1;
            bool swapL = false;
            bool swapR = false;
            while (left <= right)
            {
                if (left <= right && vow.find(s[left]) == string::npos)
                    left += 1;
                else
                    swapL = true;
                if (left <= right && vow.find(s[right]) == string::npos)
                    right -= 1;
                else
                    swapR = true;

                if (swapL == true && swapR == true)
                {
                    char temp = s[left];
                    s[left] = s[right];
                    s[right] = temp;
                    swapL = false;
                    swapR = false;
                    left += 1;
                    right -= 1;
                }
            }
        }
        return s;
    
    }

};

int main()
{
    Solution sol = Solution();
    string test_str = "leetcode";
    string res_str = sol.reverseVowels(test_str);
    cout << res_str << endl;
    string test_str2 = "Eo";
    string res_str2 = sol.reverseVowels(test_str2);
    cout << res_str2 << endl;
    return 0;
}
