class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1: Sorting (168ms: 92.48%)
        nums.sort()
        return nums[len(nums)//2]
        
        # Solution 2: Counting (296ms: 10.98%)
        dic = defaultdict(int)
        for item in nums:
            dic[item] += 1
            if dic[item] > (len(nums)//2):
                return item
        
        # Solution 3: Divide and Conquer (340ms: 5.22%)
        def find(l, r):
            if l==r: return nums[l]
            middle = (l+r)//2
            left_maj = find(l, middle)
            right_maj = find(middle+1, r)
            if left_maj == right_maj:
                return left_maj
            else:
                left_sum = sum(1 for i in range(l, middle+1) if nums[i] == left_maj)
                right_sum = sum(1 for i in range(middle+1, r+1) if nums[i] == right_maj)
                return left_maj if left_sum > right_sum else right_maj
        return find(0, len(nums)-1)
        
        # Solution 4: Boyer-Moore Voting (208ms: 35.54%)
        count = 0
        res = None
        for item in nums:
            if count == 0:
                res = item
                count += 1
            else:
                if item != res:
                    count -= 1
                else:
                    count += 1
        return res
        
        # Solution 5: Bit Manipulation (Only used on the positive numbers)
        res = 0
        i = 0
        while i < 31:
            temp = 1 << i
            num = 0
            for item in nums:
                if item & temp:
                    num += 1
            if num > (len(nums) // 2):
                res |= temp
            i += 1
        return res