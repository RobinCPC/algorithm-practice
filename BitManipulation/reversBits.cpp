/*
* #: 190
* Title: Reverse Bits
* Description:
* ------
* Reverse bits of a given 32 bits unsigned integer.
*
* For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
*                  return 964176192 (represented in binary as 00111001011110000010100101000000).
*
*
* Follow up:
* If this function is called many times, how would you optimize it?
*
*
* Related problem: Reverse Integer
*
* Credits:Special thanks to @ts for adding this problem and creating all test cases.
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Easy
*/
#include <iostream>
#include <cassert>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i=0; i < 32; ++i, n>>=1){
            res <<= 1;
            res |= n&1;
        }
        return res;
    }
};

int main(void)
{
    Solution sol = Solution();
    uint32_t n = 43261596;
    uint32_t res = sol.reverseBits(n);
    assert(res == 964176192);
    std::cout << res;
    return 0;
}
