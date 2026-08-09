class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleets = 0
        current_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > current_time:
                fleets += 1
                current_time = time

        return fleets