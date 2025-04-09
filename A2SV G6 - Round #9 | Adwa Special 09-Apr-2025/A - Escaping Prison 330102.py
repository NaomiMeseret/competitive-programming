# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    totalSum=0
    for _ in range(n):
        w,l=map(int,input().split())
        totalSum+=max(w,l)
    if totalSum<h:
        print("NO")
    else:
        print("YES")