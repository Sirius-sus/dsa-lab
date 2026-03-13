import random

n = int(input("Введите количество элементов массива: "))

numbers = [] # Объявление массива
for i in range(n):
    numbers.append(random.randint(-100, 100)) # Добавление n случайных чисел от -100 до 100

print("Исходный массив:")
print(numbers)

# Определение индексов минимального и максимального значений
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Меняем местами минимальное и максимальное значения
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Вычисляем среднее арифметическое - сумму элементов массива делим на количество
average = sum(numbers) / n
print("Среднее арифметическое:", average)

# Если элемент массива больше среднего, заменяем его на 1
for i in range(n):
    if numbers[i] > average:
        numbers[i] = 1

print("Полученный массив:")
print(numbers)
