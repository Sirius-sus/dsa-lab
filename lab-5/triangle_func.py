class IncorrectTriangleSides(Exception):
    pass 

def get_triangle_type(a, b, c):
    # Являются ли стороны числами
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise IncorrectTriangleSides("Стороны треугольника должны быть числами")

    # Являются ли стороны положительными
    elif a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными")

    # Возможно ли из заданных сторон составить треугольник
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        raise IncorrectTriangleSides("Из таких сторон нельзя составить треугольник")
    

    # Равносторонний
    elif a == b == c:
        return "equilateral"
    
    # Равнобедренный
    elif a == b or a == c or b == c:
        return "isosceles"
    
    # Обычный (разносторонний)
    else:
        return "nonequilateral"