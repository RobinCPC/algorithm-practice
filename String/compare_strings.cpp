/*
* #: 56 # lintcode
* Title: Compare Strings
* Description:
* ------
* Compare two strings A and B, determine whether A contains all of the characters in B.
* 
* The characters in string A and B are all Upper Case letters.
* 
* Example
* For A = "ABCD", B = "ABC", return true.
* 
* For A = "ABCD" B = "AABC", return false.
* ------
* Time: O(2n)
* Space: O(1)  // Constant use 256 space
* Difficulty:  Easy
*/
#include <iostream>
#include <string>
using std::string;

class Solution
{
public:
    /*!
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true
     *           else return false
     */
    bool compare_strings(string A, string B)
    {
        if(A.size() < B.size())
        {
            return false;
        }

        const int AlphabetNum = 26;
        int letterCont[AlphabetNum] = {0};
        for (int i= 0; i < A.size(); ++i)
        {
            ++letterCont[A[i] - 'A'];
        }

        for (int i = 0; i < B.size(); i++)
        {
            --letterCont[B[i] - 'A'];
            if (letterCont[B[i] - 'A'] < 0)
            {
                return false;
            }
        }

        return true;
    }

};

int main(int argc, const char *argv[])
{
    std::string A = "ABCD";
    std::string B = "ABC";
    std::string C = "AABC";

    std::cout << " A = " << A << std::endl;
    std::cout << " B = " << B << std::endl;
    std::cout << " C = " << C << std::endl;
    Solution sol = Solution();
    std::cout << "Comparing A with B..." << std::endl;
    std::cout << (sol.compare_strings(A, B)?"true":"false") << std::endl;
    std::cout << "Comparing A with C..." << std::endl;
    std::cout << (sol.compare_strings(A, C)?"true":"false") << std::endl;

    return 0;
}
