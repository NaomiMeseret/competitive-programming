# Problem: Team - https://codeforces.com/contest/231/problem/A

n=int(input())
res=0
for _ in range(n):
    countOnes=0
    num=list(map(int,input().split()))
    countOnes+=num.count(1)
    if countOnes>=2:
        res+=1
print(res)