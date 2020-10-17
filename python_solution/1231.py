class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # Solution 1: Binary Search (264ms: 58.19%)
        l, r = 1, sum(sweetness)//(K+1)
        def helper(num):
            res = temp = 0
            for i, sweet in enumerate(sweetness):
                temp += sweet
                if temp>=num:
                    res += 1
                    temp = 0
            return res>K
        while l<=r:
            mid = (l+r)//2
            if helper(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r