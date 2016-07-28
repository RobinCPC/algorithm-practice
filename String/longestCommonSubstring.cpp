/*
* #: 79     # lintcode
* Title: Longest Common Substring
* Description:
* ------
* Given two strings, find the longest common substring.
* Return the length of it.
*
* Example
* Given A="ABCD", B="CBCE", return 2.
* Note
* The characters in substring should occur continuously in original string.
* This is different with subsequence
* ------
* Time: O(mn*lcs)
* Space: O(1)           # constant
* Difficulty:  Easy
*/
#include <iostream>
#include <string>
using std::string;


class Solution
{
public:
    int longestCommonSubstring(string &A, string &B)
    {
        if (A.empty() || B.empty())
        {
            return 0;
        }
        int lcs=0, lcs_tmp=0;
        for (int i = 0; i < A.size(); ++i)
        {
            lcs_tmp = 0;
            for (int j = 0; j < B.size(); ++j) 
            {
                while ( i+lcs_tmp < A.size() &&
                        j+lcs_tmp < B.size() && 
                        A[i+lcs_tmp] == B[j+lcs_tmp]) 
                {
                    ++lcs_tmp;
                }

                // update lcs
                if (lcs_tmp > lcs) {
                    lcs = lcs_tmp;
                }
            }
        }

        return lcs;
    }

};


int main(int argc, const char *argv[])
{
    Solution sol = Solution();
    string A = "ABCD";
    string B = "CBCE";
    std::cout << sol.longestCommonSubstring(A,B) << std::endl;
    return 0;
}
