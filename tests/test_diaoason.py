import unittest
from unittest import TestCase

from base import Diapason


class DiapasonTestCase(TestCase):

    def test_diapason_str(self):
        diapason = Diapason([2, 3])
        self.assertEqual(
            first=str(diapason),
            second='Diapason([2, 3])'
        )

    def test_is_point(self):
        diapason = Diapason([0, 1.77])
        self.assertFalse(
            diapason.is_point
        )
        diapason = Diapason([1, 1.000002])
        self.assertTrue(
            diapason.is_point
        )

    def test_equal_diapasons(self):
        diapason_1 = Diapason([0, 1.77])
        diapason_2 = Diapason([0, -1])
        self.assertTrue(diapason_1.touch(diapason_2))


if __name__ == '__main__':
    unittest.main()

