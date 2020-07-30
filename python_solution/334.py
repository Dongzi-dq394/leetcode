class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Solution 1 (myself): adapted from LIS, but too complex (96ms: 20.97%)
        if not nums: return False
        stack = []
        for item in nums:
            index = bisect.bisect_left(stack, item)
            if index >= len(stack):
                stack.append(item)
                if len(stack) == 3:
                    return True
            stack[index] = item
        return False
        
        # Solution 2 from discussion: very intuitive and simple (96ms: 20.97%)
        if len(nums) < 3: return False
        first = second = float('Inf')
        for item in nums:
            if item <= first:
                first = item
            elif item <= second:
                second = item
            else:
                return True
        return False