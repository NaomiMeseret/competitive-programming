# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m=(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=[]
l,r=0,0
while l<len(a) and  r<len(b):
    if a[l]<=b[r]:
        ans.append(a[l])
        l+=1
    else:
        ans.append(b[r])
        r+=1
ans.extend(a[l:])
ans.extend(b[r:])
print(*ans)