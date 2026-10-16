import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    
    def test_zero_side_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        

    def test_huge_area(self):
        res = area(2e65)
        self.assertAlmostEqual(res, 4e130, delta = 4e130 * 1e-9)
        
    def test_huge_perimeter(self):
        res = perimeter(2e65)
        self.assertAlmostEqual(res, 8e65, delta = 8e65 * 1e-9)


    def test_typical_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_typical_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)


    def test_fractional_area(self):
        res = area(1.5)
        self.assertAlmostEqual(res, 2.25)

    def test_fractional_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 6)


    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-2)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2)


    def test_tiny_area(self):
        res = area(1e-65)
        self.assertAlmostEqual(res, 1e-130, delta = 1e-130 * 1e-9)

    def test_tiny_perimeter(self):
        res = perimeter(1e-65)
        self.assertAlmostEqual(res, 4e-65, delta = 4e-65 * 1e-9)
