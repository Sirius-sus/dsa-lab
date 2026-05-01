import unittest

from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestGetTriangleType(unittest.TestCase):
    # Позитивное тестирование
    def test_nonequilateral(self):
        result = get_triangle_type(3, 4, 5)
        self.assertEqual(result, "nonequilateral")

    def test_isosceles(self):
        result = get_triangle_type(2.5, 2.5, 3)
        self.assertEqual(result, "isosceles")

    def test_equilateral(self):
        result = get_triangle_type(7, 7, 7)
        self.assertEqual(result, "equilateral")

    # Негативное тестирование
    def test_not_number(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("а", 4, 5)

    def test_not_positive(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 4, 5)

    def test_ability(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, 8)


if __name__ == "__main__":
    unittest.main()

    