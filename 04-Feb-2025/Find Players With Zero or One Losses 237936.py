# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[match[0] for match in matches]
        losser=[match[1] for match in matches]
        losserCount=Counter(losser)
        res=[sorted([w for w in set(winner) if w not in losserCount]),sorted([l for l in (losser) if losserCount[l]==1])]
        return res


        