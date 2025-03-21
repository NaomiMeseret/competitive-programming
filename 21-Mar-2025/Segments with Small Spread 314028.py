# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
minn = deque()
maxx = deque()
left = 0

for right in range(n):
    while maxx and arr[maxx[-1]] <= arr[right]:
        maxx.pop()
    maxx.append(right)
    while minn and arr[minn[-1]] >= arr[right]:
        minn.pop()
    minn.append(right)

    while arr[maxx[0]] - arr[minn[0]] > k:
        if maxx[0] == left:
            maxx.popleft()
        if minn[0] == left:
            minn.popleft()
        left += 1

    count += (right - left + 1)

print(count)
