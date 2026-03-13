text = input("Введите строку: ")

# Объявление переменных
word = ""
result = []

# перебор каждого символа введённой строки
for char in text:
    if char != " ":
        word += char # Если не пробел, то добавляем символ к слову
    else:
        if word != "": # Проверка если слово не пустое
            if word[0] == "a" or word[-1] == "x":
                result.append(word) # Добавление в массив Result
            word = ""

# Последняя проверка вне цикла (потому что в конце строки нет пробела)
if word != "":
    if word[0] == "a" or word[-1] == "x":
        result.append(word)

print("Подходящие слова:")
for item in result:
    print(item)
