class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] >= nums[left]:
                    if target >= nums[left] and target < nums[middle]:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    if target <= nums[right] and target > nums[middle]:
                        left = middle + 1
                    else:
                        right = middle - 1
        return -1