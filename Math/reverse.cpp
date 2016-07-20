/*
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -32


time: O(logn)
space: O(1)
*/
#include <iostream>
#include <climits>   // INT_MAX, INT_MIN
using std::cout;

class Solution {
public:
    int reverse2(int x) {  // 20ms
        unsigned long r = 0;    // reverse number may bigger than int type
        int sign = 0;
        sign = (x<0)?-1:1;
        x *= sign;
        int minimum = INT_MIN, maximum = INT_MAX;
        for (; x; x /= 10)
        {
            r = r * 10 + x % 10;
        }
        if (r >= maximum) // INT_MAX = 2147483648
                return 0;
        return r*sign;
    }

    int reverse1(int x) { // 12ms
        int result = 0;
        int prev = 0;
        while(x)    // `while` will return fals if x=0
        {
            prev = result;
            result = result*10 + x%10;
            if( int(result*0.1) != prev)
            {
                return 0;
            }
            x = int(x*0.1);
        }
        return result;
    }

    int reverse(int x) { // 8ms
        int result = 0;
        while(x)
        {
            auto prev = result;
            result = result*10 + x%10;
            if( int(result*0.1) != prev)  // use '/' operator will get slower
            {
                return 0;
            }
            x = int(x*0.1);     // use '/' operator will get slower
        }
        return result;
    }

};

int main()
{
    int n = 1234567899;
    Solution sol = Solution();
    cout << sol.reverse(n)<<'\n';
    cout << sol.reverse(1234567891)<<'\n';
    cout << sol.reverse(-1234567891)<<'\n';
    cout << sol.reverse(-1234567412)<<'\n';
    cout << sol.reverse(-1234547412)<<'\n';
    return 0;
}

