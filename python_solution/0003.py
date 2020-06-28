class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
	# The first solution
	if not s: return 0
        maxlen, fast, slow = 1, 0, 0
        slen = len(s)
        dic = {}
        while fast < slen:
            if s[fast] not in dic or dic[s[fast]]==0:
                dic[s[fast]] = fast + 1
            else:
                maxlen = max(maxlen, fast-slow)
                temp = dic[s[fast]]
                dic[s[fast]] = fast + 1
                while slow < temp-1:
                    dic[s[slow]] = 0
                    slow += 1
                slow += 1
            fast += 1
        maxlen = max(maxlen, fast-slow)
        return maxlen

	# The second solution
	dic = {}
	maxlength, leftend = 0, 0
	for i in range(len(s)):
		if s[i] in dic:
			if dic[s[i]] >= leftend:
				leftend = dic[s[i]] + 1
		dic[s[i]] = i
		maxlength = max(maxlength, i-leftend+1)
	return maxlength
