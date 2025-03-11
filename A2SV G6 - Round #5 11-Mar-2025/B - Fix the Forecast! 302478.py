# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())  
for _ in range(t):
    n , k = map(int, input().split())
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))
    a = [(a[i],i) for i in range(n)]
    res = [0] * n
    a.sort()
    b.sort()
    for i in range(n):
        if abs(a[i][0]-b[i]) <=k:
            ind = a[i][1]
            res[ind] = b[i]
    print(*res)

