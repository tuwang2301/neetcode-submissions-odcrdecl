class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                b_index, b_he = stack.pop()

                if not stack:
                    break

                s_index, s_he = stack[-1]

                w = i - s_index - 1
                s = w * (min(s_he, h) - b_he)
                res += s

            stack.append((i,h))

        return res