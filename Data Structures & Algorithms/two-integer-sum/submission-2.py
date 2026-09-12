class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, n in enumerate(nums):
            other = target - n
            if other in s:
                return [s[other], i]
            s[n] = i

        return []