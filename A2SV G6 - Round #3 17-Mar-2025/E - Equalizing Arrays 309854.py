# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n=int(input())
a=list(map(int,input().split()))
m = int(input())
b =  list(map(int,input().split()))
if sum(a) != sum(b):
    print(-1)
    exit()
p1, p2 = 0,0
sum1 ,sum2=0,0
ans = 0
while p1<n:
    sum1 += a[p1]
    sum2 += b[p2]
    p1 +=1
    p2 +=1
    while sum1 != sum2:
        if sum1 < sum2:
            sum1+=a[p1]
            p1+=1
        else:
            sum2+=b[p2]
            p2+=1
    ans+=1
print(ans)