# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from math import ceil
t = int(input())
for _ in range(t):
    s = input().strip()
    length = len(s)
    x1, x2, cur1, cur2 = 0, 0, 0, 0
    flag =  False
    for i in range(length):
        remaining = length - i

        if i % 2:
            if (
                cur2 + ceil(remaining / 2) < cur1 + x1
                or cur1 + remaining // 2 < cur2 + x2
            ):
                print(i)
                flag = True
                break
            if s[i] == "1":
                cur2 += 1
            elif s[i] == "?":
                x2 += 1
        else:
            if (
                cur1 + ceil(remaining / 2) < cur2 + x2
                or cur2 + remaining // 2 < cur1 + x1
            ):
                print (i)
                flag = True
                break
            if s[i] == "1":
                cur1 += 1
            elif s[i] == "?":
                x1 += 1
    if not flag:
        print (length)