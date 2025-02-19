# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for start, e, d in shifts:
            if d == 1:
                arr[start] += d
                if e + 1 < len(arr):
                    arr[e + 1] -= d
            else:
                arr[start] -= 1
                if e+ 1 < len(arr):
                    arr[e + 1] += 1
            
        for i in range(1, len(arr)):
           arr[i] += arr[i-1]
        for i in range(len(s)):
            shift = arr[i] % 26
            arr[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        return "".join(arr[:len(s)])
