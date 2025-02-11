# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    maxNum=max(arr)
    count=[0]*100
    for num in arr:
        count[num]+=1
    return(count)