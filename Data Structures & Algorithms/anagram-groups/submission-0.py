class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}

        for s in strs:
            ssort = "".join(sorted(s))
            if ssort in anas:
                anas[ssort].append(s)
            else:
                anas[ssort] = [s]
        
        return list(anas.values())