# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

 def tupleSameProduct(self, nums: List[int]) -> int:
        productNums=defaultdict(int)
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                count+=productNums[product]*8
                productNums[product]+=1
        return count
            