class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedNum=sorted(nums)
        for i in range (0, len(sortedNum)-1):
            if sortedNum[i]==sortedNum[i+1]:
                return True
        else:
            return False
