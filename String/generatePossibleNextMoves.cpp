/*
* #: 293
* Title: Flip Game
* Description:
* ------
* You are playing the following Flip Game with your friend: Given a string that
* contains only these two characters: + and -, you and your friend take turns to
* flip two consecutive "++" into "--". The game ends when a person can no longer
* make a move and therefore the other person will be the winner.
*
* Write a function to compute all possible states of the string after one valid
* move.
*
* For example, given s = "++++", after one move, it may become one of the
* following states:
* ```
* [
*   "--++",
*   "+--+",
*   "++--"
* ]
* ```
* If there is no valid move, return an empty list [].
* ------
* Time: O(n)
* Space: O(n^2)     // worst case, a arrary to record n possible flips (each have n char)
* Difficulty:  Easy
*/

#include <iostream>
#include <string>
#include <vector>
using std::cout;
using std::string;
using std::vector;

class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> out;
        string flip = "++";
        int pos = s.find(flip);
        while (pos != -1)
        {
            string tmp = s;
            tmp.replace(pos, 2, "--");
            out.push_back(tmp);
            pos = s.find(flip, pos+1);
        }
        return out;
    }
};

int main(void)
{
    Solution obj = Solution();
    string ss = "++++";
    auto out_vec = obj.generatePossibleNextMoves(ss);
    cout << "[\n";
    for (auto i:out_vec)    // range-based for loops with auto type
    {
        cout << '\t' << i << ",\n";
    }
    cout << "]\n";
    return 0;
}
