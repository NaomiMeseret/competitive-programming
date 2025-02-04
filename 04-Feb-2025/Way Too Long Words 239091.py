# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n=int(input())
for _ in range(n):
    s=input()
    l=len(s)
    if l>10:
        print(s[0] , end="")
        print(l-2, end="")
        print(s[-1])
    else:
        print(s)