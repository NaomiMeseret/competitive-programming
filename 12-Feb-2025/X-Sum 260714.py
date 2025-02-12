# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())  
for _ in range(t):  
    n, m = map(int, input().split())  
    board = [list(map(int, input().split())) for _ in range(n)]  
    diagonal1 = {}
    diagonal2 = {}
    for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                diagonal1[d1] = diagonal1.get(d1, 0) + board[i][j]
                diagonal2[d2] = diagonal2.get(d2, 0) + board[i][j]  
    maxx = 0
    for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                total = diagonal1[d1] + diagonal2[d2] - board[i][j]
                maxx = max(maxx, total)
    print(maxx)
