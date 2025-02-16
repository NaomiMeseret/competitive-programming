# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n=int(input())
matrix=[list(map(int, input().split
())) for _ in range(n)]
goodElements=[]
middleColoumn=(n-1)//2
middleRow=(n-1)//2
for row in range(n):
    for col in range(n):
        if row==col:
            goodElements.append(matrix[row][col])
        if row + col == n - 1:
            goodElements.append(matrix[row][col])
        if row == middleRow:
            goodElements.append(matrix[middleRow][col])
        if col == middleColoumn:
            goodElements.append(matrix[row][middleColoumn])

middleSum=matrix[middleRow][middleColoumn]
totalSum=sum(goodElements)-(3* middleSum)
print(totalSum)





