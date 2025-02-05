# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount=Counter(chars)
        res=0
        for word in words:
            wordCount=Counter(word)
            if all(wordCount[char]<=charCount[char] for char in wordCount):
                res+=len(word)
        return res



        