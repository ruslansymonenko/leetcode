from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> list[int] | None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None


solution = Solution()
result = solution.two_sum([2, 7, 11, 15], 26)

print(result)