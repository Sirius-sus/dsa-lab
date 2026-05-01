class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        # Являются ли стороны числами
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise IncorrectTriangleSides("Стороны треугольника должны быть числами")

        # Являются ли стороны положительными
        elif a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Стороны треугольника должны быть положительными")

        # Возможно ли из заданных сторон составить треугольник
        elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
            raise IncorrectTriangleSides("Из таких сторон нельзя составить треугольник")
        
        else:
            self.a = a
            self.b = b
            self.c = c

    # Определение типа треугольника
    def triangle_type(self):
        # Равносторонний
        if self.a == self.b == self.c:
            return "equilateral"

        # Равнобедренный
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"

        # Разносторонний
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c