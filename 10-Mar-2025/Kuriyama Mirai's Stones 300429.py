# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n=int(input())
nums=list(map(int,input().split()))
prefixSum=[0]*n
prefixSum[0]=nums[0]
for i in range(1,len(nums)):
    prefixSum[i]=nums[i]+prefixSum[i-1]
sortedNums=sorted(nums)
sortedPrefixSum=[0]*n
sortedPrefixSum[0]=sortedNums[0]
for i in range(1,len(sortedNums)):
    sortedPrefixSum[i]=sortedNums[i]+sortedPrefixSum[i-1]
m=int(input())
for _ in range(m):
    t,l,r=map(int,input().split())
    if t==1:
        res=prefixSum[r-1]-(prefixSum[l-2] if l>1 else 0)
        print(res)
    elif t==2:
        res=sortedPrefixSum[r-1]-(sortedPrefixSum[l-2] if l>1 else 0)
        print(res)

        
