class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for key in count1.keys():
            if key in count2:
                temp = min(count1[key], count2[key])
                res += [key]*temp
        return res