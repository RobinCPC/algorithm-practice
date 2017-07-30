/*
* #: 42
* Title: Trapping Rain Water
* Description:
* ------
*
* Given n non-negative integers representing an elevation map where the width of
* each bar is 1, compute how much water it is able to trap after raining.
*
*
* For example,
* Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
*
*
* The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
* this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
* for contributing this image!
*
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Hard
*/

#include <iostream>
#include <vector>
#include <algorithm>    // std::max_element
#include <iterator>     // std::distance
using std::vector;
using std::max_element;
using std::distance;
using std::cout;

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if ( n == 0) return 0;
        // find index of maximum element (similar to argmax)
        int hi_ind = distance(height.begin(), max_element(height.begin(), height.end()));
        int max_lv = 0;
        int result = 0;
        for(int i=0; i < hi_ind; ++i){
            if (height[i] > max_lv){
                max_lv = height[i];
            }else if(height[i] < max_lv){
                result += max_lv - height[i];
            }
        }
        max_lv = 0;
        for(int i=height.size()-1; i > hi_ind; --i){
            if (height[i] > max_lv){
                max_lv = height[i];
            }else if(height[i] < max_lv){
                result += max_lv - height[i];
            }
        }
        return result;
    }
};

int main(void)
{
    Solution sol = Solution();
    vector<int> heights {0,1,0,2,1,0,1,3,2,1,2,1};
    int res = sol.trap(heights);
    cout << res << '\n';
    return 0;
}
