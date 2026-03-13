while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))

        interval = [] # Объявление массива
        for i in (a, b, c):
            if 1 <= i <= 50:
                interval.append(i) # добавление в массив, если число от 1 до 50

        print("Числа в интервале от 1 до 50:", interval)
        break

    except ValueError:
        print("Ошибка: введите числовое значение.")
