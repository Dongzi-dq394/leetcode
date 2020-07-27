class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: Hash Table (40ms: 90.51%)
        return Counter(s) == Counter(t)
        
        # Solution 2: Sort (48ms: 75.32%)
        return sorted(s) == sorted(t)