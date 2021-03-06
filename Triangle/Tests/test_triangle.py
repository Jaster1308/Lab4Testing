import unittest
from triangle import triangle_math

class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):

        self.assertEqual(12, triangle_math.area(6,4))

        self.assertAlmostEqual(17.79875, triangle_math.area(7.25, 4.91))

    def test_triangle_with_negative_input(self):

        with self.assertRaises(ValueError):
            triangle_math.area(9,-10)

        with self.assertRaises(ValueError):
            triangle_math.area(-9, 10)

        with self.assertRaises(ValueError):
            triangle_math.area(-9, -10)