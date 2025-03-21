# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        MOD = 10 ** 9 + 7
        next_smaller = [n] * n
        prev_smaller = [-1] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                prev_smaller[stack.pop()] = i
            stack.append(i)

        for i in range(n):
            cnt = (i - prev_smaller[i]) * (next_smaller[i] - i)
            res = (res + cnt * arr[i]) % MOD

        return res

        