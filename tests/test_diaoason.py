import unittest

from base import Diapason


class DiapasonTestCase(unittest.TestCase):

    def test_diapason_str(self):
        diapason = Diapason([2, 3])
        self.assertEqual(
            first=str(diapason),
            second='Diapason([2.0, 3.0])'
        )

    def test_is_point(self):
        diapason = Diapason([0, 1.77])
        self.assertFalse(
            diapason.is_point
        )
        diapason = Diapason([1, 1.0000000])
        self.assertTrue(
            diapason.is_point
        )

    def test_touch_diapasons(self):
        diapason_1 = Diapason([0, 1.77])
        diapason_2 = Diapason([0, -1])
        self.assertTrue(diapason_1.touch(diapason_2))

    def test_equal_diapasons(self):
        diapason_1 = Diapason([0, 1.77])
        diapason_3 = Diapason([0, 1.77, 1])
        diapason_2 = Diapason([0, -1])
        self.assertFalse(diapason_3 == diapason_2)
        self.assertTrue(diapason_1 == diapason_3)

    def test_in_diapason(self):
        diapason_1 = Diapason([0, 1.77])
        diapason_2 = Diapason([0, 1.77, 1])
        diapason_3 = Diapason([-2, 5])
        self.assertTrue(diapason_1 in diapason_2)
        self.assertFalse(diapason_3 in diapason_1)
        self.assertTrue(diapason_1 in diapason_3)

    def test_diapason_length(self):
        diapason_1 = Diapason([0, 1.77])
        diapason_2 = Diapason([-2, 2])
        self.assertEqual(
            diapason_1.length,
            1.77
        )
        self.assertEqual(
            diapason_2.length,
            4
        )

    def test_diapason_plus(self):
        diapason_1 = Diapason([0, 5])
        diapason_2 = Diapason([-2, 2])
        diapason = diapason_1 + diapason_2
        self.assertEqual(
            diapason.start_point,
            -2
        )
        self.assertEqual(
            diapason.end_point,
            5
        )
        self.assertEqual(
            len(diapason.points),
            4
        )

    def test_diapason_crosses(self):
        diapason_1 = Diapason([0, 5])
        diapason_2 = Diapason([5, 88])
        diapason_3 = Diapason([4, 88])
        self.assertTrue(diapason_1.crosses(diapason_2))
        self.assertFalse(diapason_1.crosses(diapason_3))
        self.assertFalse(diapason_3.crosses(diapason_2))

    def test_diapason_intersects(self):
        d_1 = Diapason([1, 3])
        d_2 = Diapason([2, 4])
        d_3 = Diapason([3, 4])
        self.assertTrue(d_1.intersects(d_2))
        self.assertFalse(d_3.intersects(d_1))
