print("Для завершения последовательности введите не число")

# Объявление счётчиков
total = 0
quantity = 0

while True:
    n = input("Введите число: ")

    try:
        number = int(n) # Преобразование ввода в integer
        total += number
        quantity += 1
        
    except ValueError: # Ошибка возникает при вводе не integer
        print("Сумма чисел последовательности:", total)
        print("Количество чисел последовательности:", quantity)
        break
