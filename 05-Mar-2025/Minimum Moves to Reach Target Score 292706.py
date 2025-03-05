# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move=0
        if maxDoubles==0:
            return target-1
        while target>1 and maxDoubles>0:
            if target%2!=0:
                move+=1
                target-=1
            else:
                target//=2
                move+=1
                maxDoubles-=1
        return move + (target-1)







            