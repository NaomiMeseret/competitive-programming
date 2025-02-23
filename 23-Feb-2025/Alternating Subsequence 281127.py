# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    totalSum = 0
    currentMax = arr[0]
    
    for i in range(1, n):
        if (arr[i] > 0) == (currentMax > 0):
            currentMax = max(currentMax, arr[i])
        else:
            totalSum += currentMax
            currentMax = arr[i]
    
    totalSum += currentMax
    print(totalSum)