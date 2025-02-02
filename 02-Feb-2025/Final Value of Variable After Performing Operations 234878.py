# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

def finalValueAfterOperations(self, operations):
        res=0
        for oper in operations:
            if oper=="--X" or oper=="X--":
                res-=1
            else:
                res+=1
        return res