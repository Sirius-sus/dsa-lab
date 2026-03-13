while True:
    try:
        m = float(input("Введите число: "))

        for i in range(1, 11):
            print(i * m) # вывод чисел от 1 * m до 10 * m 

        break

    except ValueError:
        print("Ошибка: введите числовое значение.")
