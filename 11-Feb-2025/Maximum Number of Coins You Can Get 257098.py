# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coin=0
        piles.sort()
        n=len(piles)
        l=0
        for i in range(n//3,n):
            if l%2==0:
                coin+=piles[i]
            l+=1
        return coin

        