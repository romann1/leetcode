from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> (int, int, int):
        if len(nums) == 1:
            return nums[0]

        best_sum = nums[0]  # or: float('-inf')
        best_start = best_end = 0  # or: None

        current_sum = 0
        current_start = 0
        for current_end, x in enumerate(nums):
            if current_sum <= 0:
                # Start a new sequence at the current element
                current_start = current_end
                current_sum = x
            else:
                # Extend the existing sequence with the current element
                current_sum += x

            if current_sum > best_sum:
                best_sum = current_sum
                best_start = current_start
                best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

        return best_sum, best_start, best_end


sol = Solution()
arr = [1, 2]
# arr = [-2, -10, -3, 4, -1, 2, 1, -2, 5]
# arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
arr_sum, arr_start, arr_end = sol.maxSubArray(arr)
print(f'max sub array sum of {arr} is {arr_sum}, sub-array {arr[arr_start:arr_end]}')
