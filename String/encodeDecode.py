"""
#: 271
Title: Encode and Decode Strings
Description:
------
Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of
strings.

Machine 1 (sender) has the function:

```
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```
Machine 2 (receiver) has the function:
```
vector<string> decode(string s) {
  //... your code
  return strs;
}
```
So Machine 1 does:

```
string encoded_string = encode(strs);
```
and Machine 2 does:

```
vector<string> strs2 = decode(encoded_string);
```
`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters.
Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and
decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should
implement your own encode/decode algorithm.
------
Time: O(n)
Space: O(1)     # not include output string
Difficulty: Medium
"""
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        out = ""
        for s in strs:
            out += str(len(s)) + '|' + s
        return out


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = [] 	# a list of string
        i = 0	# start point of find function
        while i < len(s):
            m = s.find('|', i)
            i = m + int(s[i:m]) + 1
            strs.append(s[m+1: i])
        return strs

if __name__ == '__main__':
    codec = Codec()
    strs = ['|Hello|', '', '|World|', '|!|', '', '', '|How |are you!|']
    #strs = ['']
    result = codec.encode(strs)
    print "result: %s" % result
    result_lst = codec.decode(result)
    print result_lst

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
