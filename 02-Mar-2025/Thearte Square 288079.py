# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

n,m,a=map(int,input().split())
countN = (n+a-1)//a
countM=(m+a-1)//a
print(countN*countM)