# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    A = input()
    B = input()
    A += "0"
    B += "0"
    valid = True
    count=0
    for i in range(n):
        if A[i]=="1":
            count+=1
        else:
            count-=1
        if count!=0:
            if A[i]!= B[i] and A[i+1] == B[i+1]:
                print("NO")
                valid = False
                break
            elif A[i]== B[i] and A[i+1] != B[i+1]:
                print("NO")
                valid = False
                break
    if valid:
        print("YES")