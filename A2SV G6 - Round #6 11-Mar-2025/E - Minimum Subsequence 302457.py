# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    stack_one=[]
    stack_zero=[]
    ans=[0]*n
    count=0
    for i in range(n):
        if s[i]=="0":
            if stack_one:
                left=stack_one.pop()
            else:
                count+=1
                left=count
 
            stack_zero.append(left)
        else:
            if stack_zero:
                left=stack_zero.pop()
            else:
                count+=1
                left=count
            stack_one.append(left)
        ans[i]=left
    print(max(ans))
    print(*ans)