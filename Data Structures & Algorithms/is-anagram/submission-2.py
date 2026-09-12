class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = [0 for _ in range(26)], [0 for _ in range(26)]
        char_a = ord('a')
        for char in s:
            cs[ord(char) - char_a] += 1
        for char in t:
            ct[ord(char) - char_a] += 1
        for i in range(26):
            if cs[i] != ct[i]:
                return False
        return True