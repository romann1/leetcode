from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_profit = 0
        best_buy = -1
        best_sell = 0

        for price in prices:
            if price < best_buy or best_buy == -1 or price < best_sell:
                best_buy = price
                best_sell = 0
                max_profit += best_profit
                best_profit = 0
            else:
                best_sell = price

            if best_sell >= best_buy:
                profit = best_sell - best_buy
                if profit > best_profit:
                    best_profit = profit

        max_profit += best_profit
        return max_profit


class TestMaxProfit(TestCase):
    def __int__(self):
        self.sol = Solution()

    def setUp(self) -> None:
        if not hasattr(self, 'sol'):
            self.sol = Solution()

    def test_price1(self):
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_price2(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_price3(self):
        self.assertEqual(self.sol.maxProfit([2, 4, 1]), 2)

    def test_price4(self):
        self.assertEqual(self.sol.maxProfit([2, 1, 2, 0, 1]), 2)

    def test_price5(self):
        self.assertEqual(self.sol.maxProfit([2, 4, 1, 7]), 8)
