"""
Solution 1:

Sliding Window, maintain a window with required char and move left/right pointers
to see what is the minimum window size that will cover all the requirements

Time Complexity: O(S + T)
Space complexity : O(S + T)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        """
        maintain a sliding window and keep counting chars seens in the window
        , start shrinking window when we have all the required chars in the window
        """
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1 
        
        # Target # of chars that source string need to match
        target = len(need)

        seen = {}
        valid = 0
        res = None
        l, r = 0, 0 
        while r < len(s):
            cur = s[r]
            seen[cur] = seen.get(cur, 0) + 1
            if cur in need and seen[cur] == need[cur]:
                valid += 1

            while valid == target:
                if not res or res[1] - res[0] > r - l:
                    res = [l, r]
                old = s[l]
                if old in need and need[old] == seen[old]:
                    valid -= 1
                seen[old] -=1
                l += 1
            r += 1
        
        return s[res[0]:res[1] + 1] if res else ""
