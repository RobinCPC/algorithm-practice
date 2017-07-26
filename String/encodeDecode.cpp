/*
* #: 271
* Title: Encode and Decode Strings
* Description:
* ------
* Design an algorithm to encode a list of strings to a string. The encoded string
* is then sent over the network and is decoded back to the original list of
* strings.
*
* Machine 1 (sender) has the function:
*
* ```
* string encode(vector<string> strs) {
*   // ... your code
*   return encoded_string;
* }
* ```
* Machine 2 (receiver) has the function:
* ```
* vector<string> decode(string s) {
*   //... your code
*   return strs;
* }
* ```
* So Machine 1 does:
*
* ```
* string encoded_string = encode(strs);
* ```
* and Machine 2 does:
*
* ```
* vector<string> strs2 = decode(encoded_string);
* ```
* `strs2` in Machine 2 should be the same as `strs` in Machine 1.
*
* Implement the `encode` and `decode` methods.
*
* Note:
* The string may contain any possible characters out of 256 valid ascii characters.
* Your algorithm should be generalized enough to work on any possible characters.
* Do not use class member/global/static variables to store states. Your encode and
* decode algorithms should be stateless.
* Do not rely on any library method such as eval or serialize methods. You should
* implement your own encode/decode algorithm.
*
* ------
* Time: O(n)
* Space: O(1)
* Difficulty: Medium
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
       string out = "";
       for (auto s : strs)
       {
           out += to_string(s.size()) + "|" + s;
       }
       return out;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> r;
        int head = 0;
        while (head < s.size())    {
            int at_pos = s.find("|", head);
            int len = stoi(s.substr(head, at_pos - head));
            head = at_pos + 1;
            r.push_back(s.substr(head, len));
            head += len;
        }

        return r;
       //vector<string> strs;
       //size_t ind = 0;
       //while (ind < s.size())
       //{
       //    int m = s.find('|', ind);
       //    int slen = stoi(s.substr(ind, m - ind));
       //    strs.push_back(s.substr(m+1, slen));
       //    ind = m + slen + 1;
       //}
       //return strs;
    }
};

int main(void)
{
    Codec codec = Codec();
    vector<string> inp = {"|Hello|", "", "|World|", "|!|", "", "", "|How |are you!|"};
    //vector<string> inp = {""};
    string out = codec.encode(inp);
    cout << out << '\n';
    vector<string> out_lst = codec.decode(out);
    for (auto s : out_lst)
    {
        cout << s << '\n';
    }
    //for (auto it: inp){
    //    cout << it << '\n';
    //}
    //return 0;
}
// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
