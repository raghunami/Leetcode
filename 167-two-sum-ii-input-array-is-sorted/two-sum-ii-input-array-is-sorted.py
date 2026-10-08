class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashSet = {}
        for i, no in enumerate(numbers):
            temp = target - no
            if temp in hashSet:
                return [hashSet[temp]+1, i+1]
            hashSet[no] = i
        return []
        