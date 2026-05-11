class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft = maxright = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                maxleft = max(maxleft, height[l])
                water += maxleft - height[l]
                l += 1
            else:
                maxright = max(maxright, height[r])
                water += maxright - height[r]
                r -= 1

        return water