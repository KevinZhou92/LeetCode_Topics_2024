"""
Solution 1:
Just loop over the string and do 3 operations:
1. Trim spaces from both end + trip multiple spaces in between the word
2. Reverse the whole string
3. Reverse each single word in the string

It is very critical we treat the pointer carefully to avoid out of index problems


Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.trim_spaces(s)
        s = self.reverse(s, 0, len(s) - 1)
        s = self.reverse_each_word(s)

        return "".join(s)
    
    def reverse_each_word(self, s):
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            self.reverse(s, start, end - 1)
            start = end + 1
            end = start
        return s
        

    def trim_spaces(self, s):
        left, right = 0, len(s) - 1
        while left < right and s[left] == " ":
            left += 1
        while left < right and s[right] == " ":
            right -= 1
        
        output = []
        while left <= right:
            if s[left] != " " or output[-1] != " ":
                output.append(s[left])
            left += 1
        
        return output
    
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        return s
        
        

