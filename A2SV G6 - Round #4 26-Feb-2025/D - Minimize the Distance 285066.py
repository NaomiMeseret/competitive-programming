# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
if n%2!=0:
    print(nums[n//2])
else:
    print(nums[(n//2)-1])