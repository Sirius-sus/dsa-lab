import pytest

from triangle_class import Triangle, IncorrectTriangleSides


# Позитивное тестирование
def test_nonequilateral():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

def test_isosceles():
    triangle = Triangle(2.5, 2.5, 3)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 8

def test_equilateral():
    triangle = Triangle(7, 7, 7)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 21


# Негативное тестирование
def test_not_number():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("а", 4, 5)

def test_not_positive():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 4, 5)

def test_ability():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 4, 8)

        