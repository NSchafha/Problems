from typing import List

class Solution:
    def convertTemperature(celsius: float) -> List[float]:
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        return [k, f]

    print(convertTemperature(4.5))