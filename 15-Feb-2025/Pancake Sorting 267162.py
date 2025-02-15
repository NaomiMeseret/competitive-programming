# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

def pancakeSort(self, arr: List[int]) -> List[int]:
        sortedNums = sorted(arr)
        res = []
        for _ in range(len(arr)):
            maxVal = sortedNums[-1]
            maxIndex = arr.index(maxVal)
            res.append(maxIndex + 1)
            arr = arr[:maxIndex + 1][::-1] + arr[maxIndex + 1:]
            res.append(len(arr))
            arr = arr[::-1]
            arr.pop()
            sortedNums.pop()
        return res
        