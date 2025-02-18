# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n=int(input())
res=[num for num in range(1000+1)]
output="".join(map(str,res))
print(output[n])