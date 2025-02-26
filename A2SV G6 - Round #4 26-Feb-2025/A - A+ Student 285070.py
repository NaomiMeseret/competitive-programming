# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t=int(input())
for _ in range(t):
    nums=list(map(int, input().split()))
    maxNum=max(nums)
    ans=[]
    count=nums.count(maxNum)
    for num in nums:
        if len(set(nums))==1:
            ans.append(1)
        elif num==maxNum and count==1:
            ans.append(0)
        elif num==maxNum and count>0:
            ans.append(1)
        else:
            ans.append(maxNum-num+1)
    print(" ".join(map(str,ans)))