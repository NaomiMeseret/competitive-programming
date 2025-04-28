# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

n=int(input())
for _ in range(n):
    n,s=map(int,input().split())
    m = (n//2)+1
    print(s//m)