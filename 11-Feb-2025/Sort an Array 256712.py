# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

 def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n <= 1:
                return nums
        mid=n//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        leftIndex=0
        rightIndex=0
        sortedArr=[]
        while leftIndex<len(left) and rightIndex<len(right):
            if left[leftIndex]<=right[rightIndex]:
                sortedArr.append(left[leftIndex])
                leftIndex+=1
            else:
                sortedArr.append(right[rightIndex])
                rightIndex+=1
        sortedArr.extend(left[leftIndex:])
        sortedArr.extend(right[rightIndex:])
        return sortedArr


        