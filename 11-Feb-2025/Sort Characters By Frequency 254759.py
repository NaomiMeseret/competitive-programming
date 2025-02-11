# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        sortedChars=sorted(freq,key=lambda c:freq[c],reverse=True)
        res=[]
        for char in sortedChars:
            res.append(char*freq[char])
        return("".join(res))

       


        



        
        