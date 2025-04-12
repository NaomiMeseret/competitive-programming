# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        def position(word):
            return int(word[-1])
        words=s.split()
        sortedWords=sorted(words,key=position)
        ans=[]
        for word in sortedWords:
            ans.append(word[:-1])
        return " ".join(ans)
        