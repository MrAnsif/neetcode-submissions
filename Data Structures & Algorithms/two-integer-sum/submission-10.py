class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                ans = sorted([i, nums.index(diff)])
                return ans