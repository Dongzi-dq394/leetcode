class NumArray:

    def __init__(self, nums: List[int]):
        self.ele = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            self.ele[i] = self.ele[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.ele[j+1]-self.ele[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)