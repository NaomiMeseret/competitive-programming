# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

 def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return 2*n