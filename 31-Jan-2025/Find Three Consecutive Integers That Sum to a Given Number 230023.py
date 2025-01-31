# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

 def sumOfThree(self, num):
        rem=num%3
        x=num//3
        result=[]
        if rem==0:
            result.extend([x-1,x,x+1])
        return result
      