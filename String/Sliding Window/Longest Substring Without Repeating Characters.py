"""
Solution 1:

Two pointer.

Template:
1. Move right to increase window
2. Move left to shrink window
3. Check answer according to question

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right = 0, 0
        seen = {}
        max_len = -sys.maxsize
        while right < len(s):
            char = s[right]
            seen[char] = seen.get(char, 0) + 1
            right += 1

            while seen[char] > 1:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    seen.pop(s[left])
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


"""
Solution 1:

Sliding Window


Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        chars = {}
        res = 0
        l = 0
        for r in range(0, len(s)):
            char = s[r]
            chars[char] = chars.get(char, 0) + 1

            while chars[char] > 1:
                chars[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
