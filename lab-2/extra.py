# Программа, которая проверяет, совпадает ли первая половина строки со второй

# asdasd = True
# asddsa = False

def compare_halfs(t):
    length = len(t) # Определяем длину строки

    if length == 0: # Если строка пустая
        print("Введена пустая строка")
        return False
    else:
        part1 = text[0 : length // 2] # Первая половина строки
        part2 = text[length // 2 :] # Вторая половина строки

        if part1 == part2:
            print("Первая половина строки СОВПАДАЕТ со второй")
            return True
        else:
            print("Первая половина строки НЕ СОВПАДАЕТ со второй")
            return False

text = input("Введите строку: ")

compare_halfs(text)
