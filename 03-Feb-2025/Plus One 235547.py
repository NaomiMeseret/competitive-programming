# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        num+=1
        return list (int(digit) for digit in str(num))