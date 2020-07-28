class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: Sorting (204ms: 55.81%)
        nums.sort()
        res = []
        # If from left to right, then there is an error in case: [4,5,5,6]
        # Because the output pattern is 'slsl...' where 's' is small, 'l' is large
        s, l = (len(nums)+1)//2-1, len(nums)-1
        while l>(len(nums)+1)//2-1:
            res.append(nums[s])
            res.append(nums[l])
            s -= 1
            l -= 1
        if len(nums)%2==1:
            res.append(nums[s])
        for i in range(len(nums)):
            nums[i] = res[i]
        
        # Solution 2: Solution 1 can be rewrite in this short way
        # Using slicing in python, very concise
        # [::-1] to reverse to avoid the case [4,5,5,6]
        #nums[:] = sorted(nums) #slower
        nums.sort() #faster
        half_len = (len(nums)+1) // 2
        nums[::2], nums[1::2] = nums[:half_len][::-1], nums[half_len:][::-1]
        
        # Solution 3: O(n) time and O(1) space
        # ...