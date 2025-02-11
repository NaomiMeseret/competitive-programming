# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

def selectionSort(self, arr):
        n=len(arr)
        for i in range(n):
            minIndex=i
            for j in range(i+1,n):
                if arr[j]< arr[minIndex]:
                    minIndex=j
            arr[minIndex],arr[i]=arr[i],arr[minIndex]
        return arr