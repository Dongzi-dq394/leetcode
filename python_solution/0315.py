class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Solution 1: Using MergeSort from discussion (212ms: 41.76%)
        if not nums: return []
        ele = [[i, n] for i, n in enumerate(nums)]
        res = [0] * len(nums)
        def MergeSort(arr):
            middle = len(arr) // 2
            if middle > 0:
                left = MergeSort(arr[:middle])
                right = MergeSort(arr[middle:])
                for i in range(len(arr)-1, -1, -1):
                    if (left and right and left[-1][1] > right[-1][1]) or not right:
                        res[left[-1][0]] += len(right)
                        arr[i] = left.pop()
                    else:
                        arr[i] = right.pop()
            return arr
        MergeSort(ele)
        return res
        
        # Solution 2: Binary Search from discussion (132ms: 86.57%)
        # bisect.bisect_left can be replace by left, right = 0, len(arr)
        if not nums: return []
        res = [0]*len(nums)
        sub_arr = []
        for i in range(len(nums)-1, -1, -1):
            index = bisect.bisect_left(sub_arr, nums[i])
            res[i] = index
            sub_arr.insert(index, nums[i])
        return res