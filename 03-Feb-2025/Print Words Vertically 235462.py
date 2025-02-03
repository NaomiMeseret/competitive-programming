# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

def printVertically(self, s: str) -> List[str]:
        res=[]
        s=s.split()
        maxLen=max(len(word) for word in s)
        for i in range(maxLen):
            col=[]
            for word in s:
                if i<len(word):
                    col.append(word[i])
                else:
                    col.append(" ")
            res.append("".join(col).rstrip())
        return res