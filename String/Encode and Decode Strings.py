"""
Solution 1:

Chunked Encoding

Time Complexity: O(N)
Space complexity : O(k)
"""


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "/:" + s

        return encodedString

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decodedStrings = []
        i = 0
        while i < len(s):
            delim = s.find("/:", i)
            length = int(s[i:delim])
            decodedStrings.append(s[delim + 2 : delim + 2 + length])
            i = delim + 2 + length

        return decodedStrings


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
