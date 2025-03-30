# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n,k=map(int,input().split())
a=list(map(int,input().split()))
if k==1:
    print(a[-1]-a[0])
elif k==n:
    print(0)
else:
    d=[]
    for i in range(1,n):
        d.append(a[i]-a[i-1])
    d.sort(reverse=True)
    maxSlice=sum(d[:k-1])
    totalCost=a[-1]-a[0]-maxSlice
    print(totalCost)