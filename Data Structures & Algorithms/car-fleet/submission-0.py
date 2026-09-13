import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        cars = [(position[i], float(target-position[i])/float(speed[i])) for i in range(len(position))]
        cars.sort(key=lambda c: c[0])

        fleets = 0
        while cars:
            pos, t = cars.pop()
            while cars and cars[-1][1] <= t:
                cars.pop()
            fleets += 1

        return fleets

        
