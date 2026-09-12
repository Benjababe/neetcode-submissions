class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(n, i) for i, n in enumerate(nums)]
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            s = nums[l][0] + nums[r][0]
            if s == target:
                return [min(nums[l][1], nums[r][1]), max(nums[l][1], nums[r][1])]
            elif s < target:
                l += 1
            else:
                r -= 1

        return []