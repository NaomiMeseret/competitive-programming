# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n,m=map(int,input().split())
a=list(map(int,input().split()))
forward=[0]*n
totalDamage=0
for i in range(1,n):
    if a[i]<a[i-1]:
        totalDamage+=a[i-1]-a[i]
    forward[i]=totalDamage
totalDamage=0
backward=[0]*n
for i in range(n-2,-1,-1):
    if a[i]<a[i+1]:
        totalDamage+=a[i+1]-a[i]
    backward[i]=totalDamage
for _ in range(m):
    s,t=map(int,input().split())
    if s<t:
        print(forward[t-1]-forward[s-1])
    else:
        print(backward[t-1]-backward[s-1])