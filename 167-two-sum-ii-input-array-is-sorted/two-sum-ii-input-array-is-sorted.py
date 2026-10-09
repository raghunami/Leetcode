class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # hashSet = {}
        # for i, no in enumerate(numbers):
        #     temp = target - no
        #     if temp in hashSet:
        #         return [hashSet[temp]+1, i+1]
        #     hashSet[no] = i
        # return []
        left = 0
        right = len(numbers) - 1
        while left<right:
            if numbers[left] +numbers[right] > target:
                right = right - 1
            elif numbers[left] +numbers[right] < target:
                left = left + 1
            else:
                return [left+1, right+1]
        return []
        