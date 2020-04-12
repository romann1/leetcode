from typing import List


class Solution:
    def __int__(self):
        pass

    def singleNumber(self, nums: List[int]) -> int:
        running_sum = 0

        for idx, x in enumerate(nums[:]):
            running_sum ^= x

        return running_sum


nums = [4, 1, 2, 1, 2]
unique_val = Solution().singleNumber(nums)
print(f'{unique_val} is unique in {nums}')
