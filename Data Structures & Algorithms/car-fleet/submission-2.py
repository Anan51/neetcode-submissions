class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cPair = [(p, s) for p, s in zip(position, speed)]
        cPair.sort(reverse=True)

        fleets = 1
        lastTime = (target - cPair[0][0]) / cPair[0][1]

        for i in range(1, len(cPair)):
            car = cPair[i]
            time = (target - car[0]) / car[1]
            if time > lastTime:
                fleets += 1
                lastTime = time

        return fleets
