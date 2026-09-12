class Solution:
    def isValid(self, s: str) -> bool:
        check = {")": "(", "}": "{", "]": "["}
        st = []
        for char in s:
            if char in "([{":
                st.append(char)
            else:
                if len(st) == 0 or st.pop() != check[char]:
                    return False
        return len(st) == 0