from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        last_zero = 0
        for idx, n in enumerate(nums):
            if n == 0 and nums[last_zero] != 0:
                last_zero = idx
            elif n != 0:
                tmp = nums[idx]
                nums[idx] = nums[last_zero]
                nums[last_zero] = tmp
                last_zero += 1


sol = Solution()
arr = [0, 1, 0, 3, 12]
print(f'{arr}')
sol.moveZeroes(arr)
print(f'{arr}')
