class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # New Solution: Binary Search (28ms: 99.82%)
        l, r = 0, len(nums)-1
        while l<=r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                # should be '<=' rather than '<'
                if nums[r] < target and nums[middle] <= nums[r]:
                    r = middle-1
                else:
                    l = middle+1
            else:
                # should be '<=' rather than '<'
                if target < nums[l] and nums[l] <= nums[middle]:
                    l = middle+1
                else:
                    r = middle-1
        return -1