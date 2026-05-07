class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = {}
        for i in nums:
            if maps.get(i) != None:
                return True
            else:
                maps[i] = 1
        return False
