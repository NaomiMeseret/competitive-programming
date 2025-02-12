# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        skill.sort()
        targetSum=skill[0]+skill[-1]
        totalSum=0
        l,r=0,n-1
        while l<r:
            if skill[l]+skill[r]!=targetSum:
                return -1
            totalSum+=skill[l]*skill[r]
            l+=1
            r-=1
        return totalSum




        

        