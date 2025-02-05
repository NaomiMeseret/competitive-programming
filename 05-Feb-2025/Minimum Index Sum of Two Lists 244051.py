# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexList1=defaultdict(int)
        indexList2=defaultdict(int)
        minIndexSum=float("inf")
        for i in range(len(list1)):
            indexList1[list1[i]]=i
        for i in range(len(list2)):
            indexList2[list2[i]]=i
        result=[]
        for word in indexList1:
            if word in indexList2:
                indexSum=indexList1[word]+indexList2[word]
                if indexSum<minIndexSum:
                    minIndexSum=indexSum
                    result=[word]
                elif indexSum==minIndexSum:
                    result.append(word)
            
        return result
        
        