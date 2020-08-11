class Solution:
    def trap(self, height: List[int]) -> int:
        # New Solution 1: Two Pointers (48ms: 92.7%)
        # Can be done in DP / Stack
        res = 0
        l, r = 0, len(height)-1
        while l<r:
            if height[l]<height[r]:
                if height[l]<=height[l+1]:
                    l += 1
                else:
                    temp = height[l]
                    start = l+1
                    while height[start]<=temp:
                        res += (temp-height[start])
                        start += 1
                    l = start
            else:
                if height[r]<=height[r-1]:
                    r -= 1
                else:
                    temp = height[r]
                    start = r-1
                    # Here is important!!!
                    while start>=l and height[start]<=temp:
                        res += (temp-height[start])
                        start -= 1
                    r = start
        return res
        
        # New Solution 2: DP (56ms: 68.90%)
        # Intuition: For each element in the array, we find the maximum level 
        # of water it can trap after the rain, which is equal to the minimum 
        # of maximum height of bars on both the sides minus its own height.
        res = 0
        if not height: return res
        
        left_max = [0]*len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max = [0]*len(height)
        right_max[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(len(height)):
            res += (min(left_max[i], right_max[i]) - height[i])
        
        return res