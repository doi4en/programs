# Функция преобразования римского числа в арабское, принимает строку
def rom_to_arab(roman):
    # Словать с возможными вариантами символов в римском числе
    dic = {"M" : 1000, "CM" : 900, "D" : 500, "CD" : 400, "C" : 100, "XC" : 90,
    "L" : 50, "XL": 40, "X" : 10, "IX" : 9, "V" : 5, "IV" : 4, "I" : 1}

    try:
        # В римском числе символы V, L, D не должны повторяться. Если вотроряются - бросаем исключение:
        if roman.count("V") > 1 or roman.count("L") > 1 or roman.count("D") > 1:
            raise KeyError
        # В Римском числе другиесимволы могут повторяться, но не более трёх раз подряд. Проверяем:
        symbol = roman[0]
        k = 0
        for symbol_next in roman:
            if symbol == symbol_next:
                k+=1
                if k > 3:
                    raise KeyError
            else:
                symbol = symbol_next
                k = 1

        # Переводим римское число в арабское
        arab = 0
        i = 0
        for roman_symbol in  dic:
            for s in roman:
                # Перебираем посимвольно римское число, если такого символа нет в словаре - бросаем исключение
                if s not in dic:
                    raise KeyError
                # Сравниваем символ из словаря с символами в римском числе,
                # если находим соответствие то увеличиваем результат на значение ключа из словаря
                if roman_symbol == roman[i:i + len(roman_symbol)]:
                    arab+=dic[roman_symbol]
                    i+=len(roman_symbol)
                    if i == len(roman):
                        # Возвращаем арабское число если доли до конца римского числа
                        return arab
                else:
                    break
    except:
        print("Incorrect input.")

# Функция преобразования арабского числа в римское, принимает целое число в диапазоне 1...3999
def arab_to_roman(input_arab):
    # Словать с возможными вариантами символов в римском числе
    dic = {1000: "M",  900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",  4: "IV", 1: "I"}

    try:
        # Римское число должно быть в диапазоне 1...3999 -> https://ru.wikipedia.org/wiki/Римские_цифры
        # иначе бросаем исключение
        if input_arab <=0 or input_arab > 3999:
            raise KeyError
        # Сравниваем ввденное арабское число со словарем
        # Если находим соответствие, то уменьшаем арабское число на значение из словаря и
        # увеличиваем римское число
        roman = ""
        for arab in  dic:
            for i in range(3):              # Каждое значение из словаря нужно проверить 3 раза, т.к. римское число может содержать
                if input_arab >= arab:      # повторяющиеся символы I, X, C, M три раза подряд
                    roman += dic[arab]
                    input_arab -= arab
        return roman
    except KeyError:
        print("Incorrect input.")

# Запрос значений у пользователя
input_number = input("Enter roman number: ")
print("Arabic number: ", rom_to_arab(input_number))
print()
input_arab = int(input("Enter arabic number beetwen 1...3999: "))
print("Roman number: ",arab_to_roman(input_arab))
