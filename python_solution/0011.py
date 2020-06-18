class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        maxwater = 0
        while end > start:
            waternow = min(height[end], height[start]) * (end-start)
            maxwater = max(maxwater, waternow)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return maxwater