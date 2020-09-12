class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Solution 1: Memoization (3444ms: 68.08%)
        strs.sort(key=lambda x: len(x))
        memo = {}
        def helper(zero, one, index):
            if (zero, one, index) in memo:
                return memo[(zero, one, index)]
            if (zero==0 and one==0) or index==len(strs):
                memo[(zero, one, index)] = 0
                return 0
            string = strs[index]
            one_num = sum(1 for char in string if char=='1')
            zero_num = len(string)-one_num
            if one_num<=one and zero_num<=zero:
                temp = max(1+helper(zero-zero_num, one-one_num, index+1), helper(zero, one, index+1))
            else:
                temp = helper(zero, one, index+1)
            memo[(zero, one, index)] = temp
            return temp
        return helper(m, n, 0)