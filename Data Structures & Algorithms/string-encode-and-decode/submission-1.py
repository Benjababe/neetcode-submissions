import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += f"{len(s)}:{s}"
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            l = 0
            while s[i] != ":":
                l = l*10 + int(s[i])
                i += 1
            i += 1
            out.append(s[i:i+l])
            i += l

        return out