class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Solution 1 from Solution: Use stack (284ms: 42.27%)
        l, r = len(nums), 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        return r-l+1 if r>l else 0
        
        # Solution 2: Sorting (200ms: 98.45%)
        temp = sorted(nums)
        if temp == nums:
            return 0
        for i in range(len(nums)):
            if temp[i]!=nums[i]:
                start = i
                break
        for i in range(len(nums)-1, -1, -1):
            if temp[i]!=nums[i]:
                end = i
                break
        return end-start+1