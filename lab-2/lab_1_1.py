while True:
    try:
        # Ввод чисел
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        c = float(input("Введите третье число: "))

        print("Минимальное число:", min(a, b, c)) # Вывод результата
        break # Завершение программы

    except ValueError:
        print("Ошибка: введите числовое значение.")
