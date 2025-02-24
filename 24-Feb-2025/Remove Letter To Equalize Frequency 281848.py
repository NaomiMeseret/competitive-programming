# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        res=len(count)
        if res==1:
            return True
        for c in list(count):
            count[c]-=1
            if count[c]==0:
                del count[c]
            if len(set(count.values()))==1:
                return True
            count[c]+=1
        return False