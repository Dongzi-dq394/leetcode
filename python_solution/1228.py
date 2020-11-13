class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # Solution: One-pass (32ms: 100.00%)
        value = arr[0] + arr[-1]
        l, r = 1, len(arr)-2
        while l<r:
            if arr[l]+arr[r]!=value:
                if abs(arr[l]-arr[l-1])>abs(arr[r+1]-arr[r]):
                    return value-arr[r]
                else:
                    return value-arr[l]
            l += 1
            r -= 1
        if l==r:
            return value-arr[l]
        else:
            return value//2