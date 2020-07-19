class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_set = string.punctuation + ' '
        s = ''.join(item for item in s if item not in p_set).lower()
        return s==s[::-1]