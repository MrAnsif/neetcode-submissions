class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures):
                # if not j:
                #     return 0
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                else:
                    j += 1
        return result
