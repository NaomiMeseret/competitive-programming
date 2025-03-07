# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+","-","*","/"}
        for char in tokens:
            if char in operations:
                if stack:
                    b=int(stack.pop())
                    a=int(stack.pop())
                    if char=="+":
                        stack.append(a+b)
                    elif char=="-":
                        stack.append(a-b)
                    elif char=="*":
                        stack.append(a*b)
                    else:
                        stack.append(int(a/b))
            else:
                stack.append(char)
        return int(stack[0])

        
        