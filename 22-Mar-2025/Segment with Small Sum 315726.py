# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s=map(int,input().split())
nums=list(map(int,input().split()))
l=0
totalSum=0
maxLength=float("-inf")
for  r in range(len(nums)):
    totalSum+=nums[r]
    while totalSum>s:
        totalSum-=nums[l]
        l+=1
    maxLength=max(maxLength,r-l+1)
print(maxLength)