class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=sorted(nums)
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                return True
        else:
            return False