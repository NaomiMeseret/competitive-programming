# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m=map(int,input().split())
grid=[input().strip() for _ in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
for i in range(n):
    for j in range(m):
        bomb_count = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                bomb_count += 1
        if grid[i][j] == '*':
            continue
        elif grid[i][j] == '.' and bomb_count != 0:
            print("NO") 
            exit()
        elif grid[i][j].isdigit() and bomb_count != int(grid[i][j]):
            print("NO")
            exit()
    
print("YES")


