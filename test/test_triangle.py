import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_fractional_perimeter(self):
        res = perimeter(3, 4, 5.2)
        self.assertAlmostEqual(res, 12.2)
        
    def test_huge_perimeter(self):
        res = perimeter(2e65, 1e65, 3e65)
        self.assertAlmostEqual(res, 6e65, delta = 6e65 * 1e-9)
        
    def test_typical_perimeter(self):
        res = perimeter(3, 2, 2)
        self.assertEqual(res, 7)

    def test_impossible_triangle_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(1, 4, 3)

    def test_zero_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 3)
            
    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 3)

    def test_tiny_perimeter(self):
        res = perimeter(1e-65, 2e-65, 1.5e-65)
        self.assertAlmostEqual(res, 4.5e-65, delta = 4.5e-65 * 1e-9)


    def test_typical_area(self):
        res = area(1, 4)
        self.assertEqual(res, 2)
        
    def test_fractional_area(self):
        res = area(2, 4.2)
        self.assertAlmostEqual(res, 4.2)
        
    def test_huge_area(self):
        res = area(1e65, 1)
        self.assertAlmostEqual(res, 5e64, delta = 5e64 * 1e-9)
        
    def test_zero_side_area(self):
        with self.assertRaises(ValueError):
            area(1, 0)
    
    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-1, 4)
    
    def test_tiny_area(self):
        res = area(1, 1e-65)
        self.assertAlmostEqual(res, 5e-66, delta = 5e-66 * 1e-9)
