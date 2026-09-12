class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0
        for n in nums:
            if (n-1) in s:
                continue

            o = n + 1
            while o in s:
                o += 1

            if (o - n) > longest:
                longest = (o - n)
        return longest