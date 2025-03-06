# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for part in logs:
            if part=="./":
                continue
            elif part=="../":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return len(stack)

        