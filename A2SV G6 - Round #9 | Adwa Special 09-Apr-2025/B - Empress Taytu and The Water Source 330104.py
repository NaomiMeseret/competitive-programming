# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    a=list(map(int,input().split()))
    def vaild(mid,n,k,d,a):
        totalTime=0
        t=0
        for i in range(n):
            if d[i]%mid==0:
                t=d[i]//mid
            else:
                t=d[i]//mid+1
            totalTime+=t*a[i]
            if totalTime>k:
                return False
        return totalTime<=k
    low=1
    high=max(d)
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if vaild(mid,n,k,d,a):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print(ans)

