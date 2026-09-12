class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums) * 2)]
        l = len(nums)
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + l] = num
        return ans