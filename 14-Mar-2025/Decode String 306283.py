# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        nums=[]
        val=0
        for char in s:
            if char.isdigit():
                val=(val*10)+int(char)
            elif char=="[":
                nums.append(val)
                stack.append(char)
                val=0
            elif char=="]":
                decodeStr=""
                while stack[-1]!="[":
                    decodeStr=stack.pop()+decodeStr
                stack.pop()
                updated = nums.pop()*decodeStr
                stack.append(updated)
            else:
                stack.append(char)
        return "".join(stack)

        
        
        