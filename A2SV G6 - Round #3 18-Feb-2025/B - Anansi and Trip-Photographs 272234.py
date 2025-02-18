# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    h=list(map(int,input().split()))
    h.sort()
    front=h[:n]
    back=h[n:]
    res=all(back[i]-front[i]>=x for i in range(n))
    if res:
        print("YES")
    else:
        print("NO")