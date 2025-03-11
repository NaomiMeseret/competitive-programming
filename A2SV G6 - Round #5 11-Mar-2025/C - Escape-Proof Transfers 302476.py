# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
p = list(map(int, input().split()))
l = 0  
count = 0  
for r in range(n): 
    if p[r] > t:
        l = r + 1   
    elif r - l + 1 >= c:
        count += 1  
print(count)
