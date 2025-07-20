from unittest import TestCase
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Find longest sub-array with matching pairs of 0 and 1s
        :param nums: list of integers
        :return: length of longest sub-array
        """
        mymap = {0: -1}
        maxlen = 0
        count = 0

        for i, x in enumerate(nums):
            count = count + (-1 if x == 0 else 1)

            if count in mymap:
                cur_len = i - mymap[count]
                maxlen = max(maxlen, cur_len)
            else:
                mymap[count] = i

        return maxlen


class TestContiguousArray(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_combo1(self):
        in_list = [0, 1]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(2, result, in_list)

    def test_combo2(self):
        in_list = [0, 1, 1, 0, 1, 1, 1, 0]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(4, result, in_list)

    def test_combo3(self):
        in_list = [0, 0, 0, 1, 1, 1, 0]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(6, result, in_list)

    def test_combo4(self):
        in_list = [0, 1, 0]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(2, result, in_list)

    def test_combo5(self):
        in_list = [0, 0, 1, 0, 0, 0, 1, 1]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(6, result, in_list)

    def test_combo6(self):
        in_list = [0, 1, 0, 0, 1, 1, 0]
        result = self.sol.findMaxLength(in_list)
        self.assertEqual(6, result, in_list)