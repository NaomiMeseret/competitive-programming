# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count=Counter(words[0])
        ans=[]
        for i in range(1,len(words)):
            currentCount = Counter(words[i])
            temp={}
            for char in count:
                if char in currentCount:
                    temp[char]=min(count[char],currentCount[char])
                else:
                    temp[char]=0
            count=temp
        for char,freq in count.items():
            ans.extend(char*freq)
        return ans