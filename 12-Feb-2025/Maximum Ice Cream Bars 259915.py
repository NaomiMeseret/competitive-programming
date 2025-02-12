# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxCosts=max(costs)
        count=[0]*(maxCosts+1)
        for cost in costs:
            count[cost]+=1
        target=0
        for index,value in enumerate(count):
            for i in range(value):
                costs[target]=index
                target+=1
        Sum=0
        res=0
        for cost in costs:
            Sum+=cost
            if Sum<=coins:
                res+=1
            else:
                break
        return res


        

        

        
        