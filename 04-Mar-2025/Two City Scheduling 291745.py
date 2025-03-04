# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)//2
        def sortedCosts(cost):
            return cost[1]-cost[0]
        costs.sort(key=sortedCosts)
        totalCost=0
        for i in range(n):
            totalCost+=costs[i][1]
        for i in range(n,2*n):
            totalCost+=costs[i][0]
        return totalCost


        