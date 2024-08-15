"""
Solution 1:

Stack

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        stack = []
        idx = 0
        cnt = 0
        curString = []
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                cnt = cnt * 10 + int(c)
            elif c.isalpha():
                curString.append(c)
            elif c == "[":
                stack.append((cnt, curString))
                curString = []
                cnt = 0
            else:
                prevCnt, prevString = stack.pop()
                prevString.extend(prevCnt * curString)
                curString = prevString
            idx += 1

        return "".join(curString)


"""
Solution 2:

Count Stack + String Stack


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        countStack = []
        stringStack = []

        idx = 0
        num = 0
        string = []
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                string.append(c)
            elif c == "[":
                countStack.append(num)
                num = 0
                stringStack.append(string)
                string = []
            else:
                count = countStack.pop()
                prevString = stringStack.pop()
                prevString.extend(string * count)
                string = prevString
            idx += 1

        return "".join(string)
