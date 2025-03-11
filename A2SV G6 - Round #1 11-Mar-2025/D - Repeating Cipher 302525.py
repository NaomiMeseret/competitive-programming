# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n=int(input())
s=input()
res=[]
i = 0
step = 1
while i < n:
    res.append (s[i])
    i += step
    step += 1
print("".join(res))