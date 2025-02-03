# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res=[]
        kelvin=celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        res.extend([kelvin,Fahrenheit])
        return res


        