class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        dic = defaultdict(int)
        dic[0] = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            res += dic[cur_sum-k]
            dic[cur_sum] += 1
        return res