# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        newWord1="".join(word1)
        newWord2="".join(word2)
        if newWord1==newWord2:
            return True
        else:
            return False
        