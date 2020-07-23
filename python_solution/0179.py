class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            a, b = str(a), str(b)
            a, b = a*len(b), b*len(a)
            for i in range(len(a)):
                if a[i] > b[i]:
                    return True
                elif a[i] < b[i]:
                    return False
            return True
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        nums.reverse()
        res = ''.join(str(item) for item in nums)
        return '0' if res[0]=='0' else res