isCorrect = False
while not isCorrect:
    value = input("Введите число (точка - конец ввода): ")
    isCorrect = value.lstrip('-').isdigit()
    if not isCorrect:
        print("значение введено некорректно")
number = int(value)
minimum = number
maximum = number
value = input("Введите число (точка - конец ввода): ")
while value!=".":
    isCorrect = value.lstrip('-').isdigit()
    if not isCorrect:
        print("значение введено некорректно")
    else:
        number = int(value)
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    value = input("Введите число (точка - конец ввода): ")
print("Минимум равен %d" % minimum)
print("Максимум равен %d" % maximum)
