"""
#: 288
Title: Unique Word Abbreviation
Description:
------
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:
```
a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
```
Assume you have a dictionary and given a word, find whether its abbreviation is
unique in the dictionary. A word's abbreviation is unique if no other word from
the dictionary has the same abbreviation.

Example:
```
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") ->
false

isUnique("cart") ->
true

isUnique("cane") ->
false

isUnique("make") ->
true
```
------
Time: O(1)  # time for looking up dict, but need O(n) to construct dict
Space: O(k) # unique key word
Difficulty: Easy
"""

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr = {}
        for w in dictionary:
            ab = self.getAbbr(w)
            if ab not in self.abbr:
                self.abbr[ab] = w
            elif ab in self.abbr and w != self.abbr[ab]:
                self.abbr[ab] += '2'
        #print self.abbr


    def getAbbr(self, word):
        if len(word) > 2:
            return word[0] + str(len(word[1:-1])) + word[-1]
        else:
            return word


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        ab = self.getAbbr(word)
        if ab in self.abbr and word == self.abbr[ab]:
            return True
        return ab not in self.abbr

if __name__ == '__main__':
    dictionary = ["deer", "door", "cake", "card", "dog", "hello", "dig", "a", "a"]
    vwa = ValidWordAbbr(dictionary)
    print vwa.isUnique("dear")
    print vwa.isUnique("cart")
    print vwa.isUnique("cane")
    print vwa.isUnique("make")
    print vwa.isUnique("")
    print vwa.isUnique("hello")
    print vwa.isUnique("dog")
    print vwa.isUnique("a")

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")

