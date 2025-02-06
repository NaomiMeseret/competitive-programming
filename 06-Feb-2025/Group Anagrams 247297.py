# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for word in strs:
            strSorted="".join(sorted(word))
            anagram[strSorted].append(word)
        return list(anagram.values())
        
        