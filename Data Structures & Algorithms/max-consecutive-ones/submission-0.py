class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, mc = 0, 0
        for n in nums:
            if n == 1:
                c += 1
                if c > mc:
                    mc = c
            else:
                c = 0
        return mc