/*
 Write a function that takes a string as input and returns the string reversed.
 
 Example:
 Given s = "hello", return "olleh".
*/

#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::endl;

class Solution {
public:
    string reverseString(string s) {
        size_t n = s.size();
        if (n <= 1)
        {
            return s;
        }
        else
        {
            int n_f = int(n*0.5);
            for (int i = 0; i < n_f; ++i)
            {
                char temp = s.at(i);
                s.at(i) = s.at(n-1-i);
                s.at(n-1-i) = temp;
            }
            return s;
        }
    }
};


int main()
{
    string inp_str = string("Hello World!");
    Solution sol = Solution();
    cout << sol.reverseString(inp_str) << endl;

    return 0;
}
