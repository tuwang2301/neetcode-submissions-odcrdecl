class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        dic = {}
        for i, p in enumerate(position):
            dic[p] = speed[i]

        stack = []
        position.sort()
        for p in position:
            time = (target - p) / dic[p]
            stack.append(time)

        count = 0
        curr_time = 0
        while stack:
            if curr_time < stack[-1]:
                count += 1
                curr_time = stack[-1]
            stack.pop()

        return count
