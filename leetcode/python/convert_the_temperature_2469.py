from typing import List


class Solution:


    def convertTemperature(self, celsius: float) -> List[float]:

        to_fahrenheit = lambda x: x*1.8 + 32
        to_kelvin = lambda x: x+273.15

        return [to_kelvin(celsius), to_fahrenheit(celsius)]


print(Solution().convertTemperature(celsius = 36.50))

