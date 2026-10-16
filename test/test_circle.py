import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    
    def test_zero_rad_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_rad_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_typical_area(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_typical_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)


    def test_huge_area(self):
        res = area(2e65)
        self.assertAlmostEqual(res, 4e130 * math.pi, delta = 4e130 * math.pi * 1e-9)
        
    def test_huge_perimeter(self):
        res = perimeter(2e65)
        self.assertAlmostEqual(res, 4e65 * math.pi, delta = 4e65 * math.pi * 1e-9)
        
        
    def test_negative_rad_area(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_negative_rad_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


    def test_tiny_area(self):
        res = area(1e-65)
        self.assertAlmostEqual(res, 1e-130 * math.pi, delta = 1e-130 * math.pi * 1e-9)

    def test_tiny_perimeter(self):
        res = perimeter(1e-65)
        self.assertAlmostEqual(res, 2e-65 * math.pi, delta = 2e-65 * math.pi * 1e-9)


    def test_fractional_area(self):
        res = area(1.5)
        self.assertAlmostEqual(res, 2.25 * math.pi)

    def test_fractional_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 3 * math.pi)
