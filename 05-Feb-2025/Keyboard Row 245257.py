# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        res = []
        for word in words:
            wordLower = word.lower()
            if all(char in row1 for char in wordLower):
                res.append(word)
            elif all(char in row2 for char in wordLower):
                res.append(word)
            elif all(char in row3 for char in wordLower):
                res.append(word)
        return res