class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Solution from Solution: Sort + Two Pointers (120ms: 87.56%)
        # A very good question
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            remain = target-nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                temp = nums[l]+nums[r]
                if temp<remain:
                    res += r-l
                    l += 1
                else:
                    r -= 1
        return res