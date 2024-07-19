"""
Solution 1:

Generate all potential substrings and count duplicates
Find the substring with longest length

Memory Limit Exceeded!

Time Complexity: O(N^3)
Space complexity : O(N^2)
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        if not s:
            return ""

        duplicates = {}
        for i in range(0, len(s)):
            for j in range(0, i + 1):
                substring = s[j : i + 1]
                if not substring:
                    continue
                duplicates[substring] = duplicates.get(substring, 0) + 1

        ans = ""
        for key in duplicates:
            if duplicates[key] > 1 and len(key) > len(ans):
                ans = key

        return ans


"""
Solution 2:

Binary Search + Rabin Karp

Don't do repetitive calculation of base ** targetLength

Time Complexity: O(NlogN)
Space complexity : O(N)
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        if not s:
            return ""

        # start and end length
        start = 1
        end = len(s)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.search(s, mid) >= 0:
                start = mid
            else:
                end = mid
        
        index =  self.search(s, end)
        if index >= 0:
            return s[index: index + end]

        index =  self.search(s, start)
        if index >= 0:
            return s[index: index + start]
        
        return ""
        
    def search(self, s, targetLength):
        visited = collections.defaultdict(list)
        hashValue = 0
        base = 31
        mod = 2**63 - 1
        baseL = pow(base, targetLength - 1, mod)

        for i in range(0, len(s)):
            if i < targetLength:
                hashValue = (hashValue * base + ord(s[i])) % mod
            else:
                visited[hashValue].append(i - targetLength)
                hashValue = ((hashValue - ord(s[i - targetLength]) * baseL) * base + ord(s[i])) % mod
            
            if hashValue in visited:
                startIndex = visited[hashValue][0]
                curString = s[startIndex: startIndex + targetLength]
                if any(curString == s[index : index + targetLength] for index in visited[hashValue]):
                    return startIndex
        
        return -1

            

        