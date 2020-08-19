class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: 84ms
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        # Solution 2: Reverse (64ms: 77.43%)
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
        # New Solution 3: Cyclic Replacements from Solution (84ms: 46.21%)
        start = 0
        count = 0
        length = len(nums)
        while count<length:
            cur_ind, pre_val = start, nums[start]
            while True:
                new_ind = (cur_ind+k)%length
                nums[new_ind], pre_val = pre_val, nums[new_ind]
                cur_ind = new_ind
                count += 1
                if new_ind == start:
                    break
            start += 1