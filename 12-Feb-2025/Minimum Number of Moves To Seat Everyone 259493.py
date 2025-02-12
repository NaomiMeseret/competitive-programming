# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sortedSeats=sorted(seats)
        sortedStudent=sorted(students)
        Sum=0
        l,r=0,0
        while l<len(sortedSeats) and r<len(sortedStudent):
            Sum+=abs(sortedSeats[l]-sortedStudent[r])
            l+=1
            r+=1
        return Sum

        



        