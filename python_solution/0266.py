class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Solution 1: Hash Table (28ms: 72.39%)
        count = Counter(s)
        remain = 1 if len(s)%2==1 else 0
        for key in count:
            if count[key]%2==1:
                if remain==0:
                    return False
                remain -= 1
        return True