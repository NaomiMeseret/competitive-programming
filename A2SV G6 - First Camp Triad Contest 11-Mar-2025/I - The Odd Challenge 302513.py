# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t=int(input())
for _ in range(t):
    n,q = map(int,input().split())
    a=list(map(int,input().split()))
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+a[i]
    total=prefix[-1]
    res=[]
    for _ in range(q):
        l,r,k=map(int,input().split())
        rOldSum=prefix[r]-prefix[l-1]
        rNewSum = (r-l+1)*k
        newSum=total - rOldSum + rNewSum
        if newSum %2==1:
            print("YES")
        else:
            print("NO")

