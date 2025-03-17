# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict
k = int(input())
s = input()
onesCount = 0
count = 0
f = {0: 1}

for char in s:
    if char == '1':
        onesCount += 1
    count += f.get(onesCount - k, 0)
    f[onesCount] = f.get(onesCount, 0) + 1
print(count)