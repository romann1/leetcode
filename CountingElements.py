from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        elements = {}
        for x in arr:
            elements[x] = True

        count = 0
        for x in arr:
            if (x + 1) in elements:
                count += 1

        return count


sol = Solution()
print(f'{sol.countElements([1, 3, 2, 3, 5, 0])}')
