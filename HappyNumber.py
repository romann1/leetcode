from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        num_iter = 0
        sum_digits = 0
        while sum_digits != 1 and num_iter < 20:
            sum_digits = 0
            digits = self.__get_digits(n)
            for d in digits:
                sum_digits += pow(d, 2)
            n = sum_digits
            num_iter += 1

        if num_iter == 20:
            return False

        return True

    def __get_digits(self, n: int) -> List[int]:
        digit_str = str(n)
        return [int(d) for d in digit_str]


sol = Solution()
n = 29
print(f'{sol.isHappy(n)}')
