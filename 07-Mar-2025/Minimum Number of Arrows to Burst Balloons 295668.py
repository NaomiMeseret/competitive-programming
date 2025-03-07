# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def sortedNum(point):
            return point[1]
        points.sort(key=sortedNum)
        arrow=0
        c=float("-inf")
        for point in points:
            if point[0] >c:
                arrow+=1
                c=point[1]
        return arrow