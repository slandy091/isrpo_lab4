import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    
    def test_zero_side_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)


    def test_typical_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_typical_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)


    def test_huge_area(self):
        res = area(2e65, 1e65)
        self.assertAlmostEqual(res, 2e130, delta = 2e130 * 1e-9)
        
    def test_huge_perimeter(self):
        res = perimeter(2e65, 1e65)
        self.assertAlmostEqual(res, 6e65, delta = 6e65 * 1e-9)


    def test_fractional_area(self):
        res = area(2.5, 3.2)
        self.assertAlmostEqual(res, 8)

    def test_fractional_perimeter(self):
        res = perimeter(2.5, 3.2)
        self.assertAlmostEqual(res, 11.4)


    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-3, 5)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 5)


    def test_tiny_area(self):
        res = area(2e-65, 1e-65)
        self.assertAlmostEqual(res, 2e-130, delta = 2e-130 * 1e-9)

    def test_tiny_perimeter(self):
        res = perimeter(2e-65, 1e-65)
        self.assertAlmostEqual(res, 6e-65, delta = 6e-65 * 1e-9)
