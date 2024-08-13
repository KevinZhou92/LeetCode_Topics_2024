"""
Solution 1:

Use a stack to track parenthese, pop matching parenthese. We will have an empty stack if everything matches.

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def isValid(self, str: str) -> bool:
        stack = []
        for c in str:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if stack and self.leftOf(c) == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack

    def leftOf(self, c: str) -> str:
        if c == "}":
            return "{"
        if c == ")":
            return "("
        if c == "]":
            return "["

        return ""
