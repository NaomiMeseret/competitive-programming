# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    left=defaultdict(int)
    right=Counter(s)
    maxAns=0
    for char in s:
        ans=len(right)+ len(left)
        maxAns=max(maxAns,ans)
        left[char]+=1
        if char in right:
           right[char]-=1
           if right[char]==0:
                del right[char]
    print (maxAns)