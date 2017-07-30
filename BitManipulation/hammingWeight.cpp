
/*
* #: 191
* Title: Number of 1 Bits
* Description:
* ------
* Write a function that takes an unsigned integer and returns the number of '1' bits
* it has (also known as the Hamming weight).
*
* For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
* so the function should return 3.
*
* Credits:Special thanks to @ts for adding this problem and creating all test cases.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Easy
*/
#include <iostream>
#include <climits>
#include <cassert>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while (n){
            n = n & (n-1);
            cnt += 1;
        }
        return cnt;
    }
};

int main(void)
{
    Solution sol = Solution();
    unsigned int n = UINT_MAX;
    int nbits = sol.hammingWeight(n);
    assert(nbits == 32);
    std::cout << nbits << '\n';
    return 0;
}
