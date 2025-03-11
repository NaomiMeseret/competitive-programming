# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n,k=map(int,input().split())
nums=list(map(int,input().split()))
queue=deque()
seen=set()
for num in nums:
    if num in seen:
        continue
    elif len(queue)==k:
        r = queue.popleft()
        seen.remove(r)
    queue.append(num)
    seen.add(num)
queue.reverse()
print(len(queue))
print(*queue)


