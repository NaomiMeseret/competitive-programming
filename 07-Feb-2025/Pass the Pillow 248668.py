# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction=1
        i=1
        while time>0:
            i+=direction
            if i>n:
                i=n-1
                direction=-1
            elif i<1:
                i=2
                direction=1
            time-=1

        return i

            
            




        