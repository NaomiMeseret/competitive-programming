# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t=int(input())
for _ in range(t):
    word=input()
    res=0
    target="codeforces"
    for i in range(len(target)):
        if word[i]!=target[i]:
            res+=1
    print(res)