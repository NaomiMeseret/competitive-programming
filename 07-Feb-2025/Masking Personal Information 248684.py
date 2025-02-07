# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s=s.lower()
            name,domain=s.split("@")
            Maskedname= name[0]+"*"*(5) +name[-1]
            return(Maskedname+"@"+domain)
        else:
            digits=[c for c in s if c.isdigit()]
            localNumber="".join(digits[-4:])
            countryCodeLength=len(digits)-10
            if countryCodeLength==0:
                return ("***-***-"+localNumber)
            else:
                return("+"+ "*"*countryCodeLength+"-***-***-"+localNumber)
            

            



        