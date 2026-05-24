class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            maxLength = max(maxLength, r - l + 1)
            window.add(s[r])

        return maxLength