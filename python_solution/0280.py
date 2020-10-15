class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: Sort (92ms: 84.10%)
        nums.sort()
        temp = []
        ind = -1
        for i in range((len(nums)-1)//2, -1, -1):
            temp.append(nums[i])
            temp.append(nums[ind])
            ind -= 1
        if len(nums)%2:
            temp.pop()
        nums[:] = temp[:]
        
        # Solution 2 from discussion: One-pass
        # Since we accept the 'equal', the constrain
        # is not to strong. We just need to compare
        # two elements each time.
        # While, for the stronger condition, we need sort.
        for i in range(len(nums)-1):
            if (i%2==0 and nums[i]>nums[i+1]) or (i%2==1 and nums[i]<nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]