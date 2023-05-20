import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        """Проверка с пустым массивом"""
        self.assertEqual(arrs.my_slice([], 0, 2), [])
        """Проверка с отрицательным start и end None"""
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3), [2, 3, 4])
        """Проверка со start=0 и end None"""
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0), [1, 2, 3, 4])
        """проверка если старт меньше -длинны строки"""
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -10, 2), [1, 2])