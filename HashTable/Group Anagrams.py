"""
Solution 1:

HashTable + Sorting

Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs)
Space complexity : O(NK)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagrams = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(list(s)))
            anagrams[sortedS].append(s)

        return anagrams.values()


"""
Solution 2:

HashTable + Encode

Time Complexity: O(NK)
Space complexity : O(NK)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)

        return anagrams.values()
        