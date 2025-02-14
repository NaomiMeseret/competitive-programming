# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n,s=map(int,input().split())
a=list(map(int,input().split()))
count=0
l=0
seen={}
ans=[float("inf"),float("-inf")]
for r in range(n):
    seen[a[r]]=seen.get(a[r],0)+1
    while len(seen)>s:
        seen[a[l]]-=1
        if seen[a[l]]==0:
            del seen[a[l]]
        l+=1
    if r-l>ans[1]-ans[0]:
        ans=[l+1,r+1]
print(*ans)
  