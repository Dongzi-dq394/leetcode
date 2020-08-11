class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # New Solution: Three Binary Search (80ms: 97.85%)
        l, r = 0, len(nums)-1
        while l<=r:
            middle = (l+r)//2
            if nums[middle] == target:
                break
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        if l > r:
            return [-1,-1]
        left = right = middle
        temp = middle
        while l<=temp:
            mid = (l+temp)//2
            if nums[mid] == target:
                left = min(left, mid)
                temp = mid - 1
            else:
                l = mid + 1
        temp = middle
        while temp<=r:
            mid = (temp+r)//2
            if nums[mid] == target:
                right = max(right, mid)
                temp = mid + 1
            else:
                r = mid - 1
        return [left, right]