# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

 def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        count=Counter(nums)
        for num in nums:
            if count[num]>n//3:
                res.append(num)
        return list(set(res))