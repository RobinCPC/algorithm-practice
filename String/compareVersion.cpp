/*
 * #: 165
 * Title: Compare Version Numbers
 * Description:
 * ------
 * Compare two version numbers version1 and version2.
 * If version1 &gt; version2 return 1, if version1 &lt; version2 return -1, otherwise return 0.
 * 
 * You may assume that the version strings are non-empty and contain only digits and the . character.
 * The . character does not represent a decimal point and is used to separate number sequences.
 * For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
 * 
 * Here is an example of version numbers ordering:
 * `
 * 0.1 < 1.1 < 1.2 < 13.37
 * `
 * 
 * Credits:Special thanks to @ts for adding this problem and creating all test cases.
 * ------
 * Time: O(n)
 * Space: O(n)
 * Difficulty: Medium
 **/
#include <iostream>     // std::cout
#include <string>       // std::string
#include <sstream>      // std::stringstream
#include <cassert>
using namespace std;

// source: https://discuss.leetcode.com/topic/92226/simple-c-10-line-solution-using-stringstream
class Solution {
public:
    int compareVersion(string version1, string version2) {
        stringstream ss1(version1), ss2(version2);
       char _; //dummy var 
       while(true){
           int n1 = 0, n2 = 0; // re-initialized.
           ss1 >> n1;   // get integer from string streams
           ss2 >> n2;
           if(ss1.fail() && ss2.fail())
               return 0;
           else if (n1 > n2)
               return 1;
           else if (n1 < n2)
               return -1;
           ss1 >> _;    // put '.' in dummy variable
           ss2 >> _;
       }

    }
};


int main(void)
{
    Solution sol = Solution();
    string ver1 = "1.32.0.000.0.1";
    string ver2 = "1.32.0.000.0.3";
    cout << sol.compareVersion(ver1, ver2);
    assert( sol.compareVersion(ver1, ver2) == -1);
    return 0;
}

