# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int: 
        total_drunk = numBottles  
        while numBottles >= numExchange:   
            new_bottles = numBottles // numExchange   
            total_drunk += new_bottles  
            numBottles = new_bottles + (numBottles % numExchange)  
        
        return total_drunk
        