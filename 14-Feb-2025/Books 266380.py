# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t =map(int,input().split())
a=list(map(int,input().split()))
l=0
Sum=0
maxLength=0
for r in range(len(a)):
    Sum+=a[r]
    while Sum>t:
        Sum-=a[l]
        l+=1
    maxLength=max(maxLength,r-l+1)
print(maxLength)