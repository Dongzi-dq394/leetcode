class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                first = last = middle
                right_temp, left_temp = middle - 1, middle + 1
                while left <= right_temp:
                    middle_temp = (left + right_temp) // 2
                    if nums[middle_temp] == target:
                        first = middle_temp
                        right_temp = middle_temp - 1
                    else:
                        left = middle_temp + 1
                while left_temp <= right:
                    middle_temp = (left_temp + right) // 2
                    if nums[middle_temp] == target:
                        last = middle_temp
                        left_temp = middle_temp + 1
                    else:
                        right = middle_temp - 1
                return [first, last]
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return [-1, -1]