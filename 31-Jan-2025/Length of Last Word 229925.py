# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

    def lengthOfLastWord(self, s):
        word=s.split()
        return(len(word[-1]))