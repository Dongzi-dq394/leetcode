class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Solution 1: by myself, Hash Table + Recursion (24ms: 98.82%)
        if len(s)<k: return 0
        count = Counter(s)
        ele = {}
        for key in count.keys():
            if count[key] < k:
                ele[key] = True
        slow = fast = 0
        res = 0
        while fast<len(s):
            if s[fast] in ele:
                res = max(res, self.longestSubstring(s[slow:fast], k))
                fast += 1
                slow = fast
            else:
                fast += 1
        if slow==0:
            return len(s)
        res = max(res, self.longestSubstring(s[slow:fast], k))
        return res
        
        # Solution 2: from discussion (36ms: 75.99%)
        for item in set(s):
            if s.count(item) < k:
                return max(self.longestSubstring(subs, k) for subs in s.split(item))
        return len(s)