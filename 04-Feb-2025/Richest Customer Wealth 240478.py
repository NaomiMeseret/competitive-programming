# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=0
        for account in accounts:
            maxWealth=max( maxWealth, sum(account))
        return maxWealth