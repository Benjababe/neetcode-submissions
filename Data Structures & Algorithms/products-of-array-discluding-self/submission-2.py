class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr = [1] * len(nums)
        for i, n in enumerate(nums):
            lr[i] = lr[i-1] * n
        
        out = [1] * len(nums)
        rl = 1
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                out[i] = rl
            elif i == len(out)-1:
                out[i] = lr[i-1]
            else:
                out[i] = lr[i-1] * rl

            if i < len(nums)-1:
                rl = rl * nums[i]
            else:
                rl = nums[i]

        return out