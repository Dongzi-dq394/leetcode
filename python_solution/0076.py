class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # New Solution: one-pass + defaultdict (68ms: 99.89%)
        if not t: return ''
        dic = defaultdict(int)
        length = 0 # Total number in t
        for char in t:
            dic[char] += 1
            length += 1
        min_length = float('Inf')
        start = 0
        res = ''
        for i, char in enumerate(s):
            if dic[char]>0:
                # Meaning: we still need this char to build the target string
                length -= 1
            # We will always subtract 1
            dic[char] -= 1
            if length == 0:
                # For those char that has negative value in dict, we just ignore it
                # because it is not neccessary for the target string
                while dic[s[start]]<0:
                    dic[s[start]] += 1
                    start += 1
                # Compare and Re-Assign
                if i-start+1<min_length:
                    min_length = i-start+1
                    res = s[start:i+1]
                dic[s[start]] += 1
                length += 1 # Important!
                start += 1
        return res