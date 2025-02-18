# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
t=int(input())
for _ in range(t):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    window=Counter(a[:d])
    minLength=len(window)
    l=0
    for i in range(d,len(a)):
        window[a[i]]+=1
        window[a[i-d]]-=1
        if window[a[i-d]]==0:
            del window[a[i-d]]
        minLength=min(minLength,len(window))
    print(minLength)
