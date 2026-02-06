class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        result = [candy + extraCandies >= max_num for candy in candies]
        # result = []
        # for candy in candies:
        #     if candy + extraCandies >= max_num:
        #         result.append(True)
        #     else:
        #         result.append(False)
        return result
        