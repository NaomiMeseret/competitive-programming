# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q=map(int,input().split())
diff=[0]*200002
for _ in range(n):
    l,r=map(int,input().split())
    diff[l]+=1
    diff[r+1]-=1
for i in range(1,len(diff)):
    diff[i]+=diff[i-1]
for j in range(len(diff)):
    if diff[j]>=k:
        diff[j]=1
    else:
        diff[j]=0
for i in range(1,len(diff)):
    diff[i]+=diff[i-1]
for _ in range(q):
    l,r=map(int,input().split())
    if diff[l]==0:
        print(diff[r])
    else:
        print(diff[r]-diff[l-1])