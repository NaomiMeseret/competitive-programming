# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxValue=max(candies)
        res=[]
        for candie in candies:
            candie+=extraCandies
            if candie>=maxValue:
                res.append(True)
            else:
                res.append(False)
        return res