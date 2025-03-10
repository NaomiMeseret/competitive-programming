# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    current_sum = 0
    maxRed = 0
    for num in r:
        current_sum += num
        if current_sum > maxRed:
            maxRed = current_sum
    
    current_sum = 0
    maxBlue = 0
    for num in b:
        current_sum += num
        if current_sum > maxBlue:
            maxBlue = current_sum
    print(maxBlue + maxRed)

