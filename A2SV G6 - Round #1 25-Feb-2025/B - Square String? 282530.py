# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t=int(input())
for _ in range(t):
    word=input()
    res=len(word)//2
    if word[0:res] ==word[res:] and len(word)%2==0:
        print("YES")
    else:
        print("NO")