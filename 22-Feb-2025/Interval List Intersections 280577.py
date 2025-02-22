# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        x, y = 0, 0
        res = []
        while x < len(firstList) and y < len(secondList):
            s1, e1 = firstList[x]
            s2, e2 = secondList[y]
            start = max(s1, s2)
            end = min(e1, e2)
            if start <= end:
                res.append([start, end])
            if e1 < e2:
                x += 1
            else:
                y += 1
        return res