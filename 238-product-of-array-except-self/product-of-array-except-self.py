class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [1] * nums_length

        left_product = 1
        for i in range(nums_length):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(nums_length-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result