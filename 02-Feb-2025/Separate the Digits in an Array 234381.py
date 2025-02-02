# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

def separateDigits(self, nums):
        res=[]
        for num in nums:
            if num>=10:
                res.extend(int(digit) for digit in str(num))
            else:
                res.append(num)
        return res