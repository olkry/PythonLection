# print(5, 8, 6)

# n = 1.89
# print(n)

# n="fddf"
# print(n)

# n1 = 'vvjdfjh'

# # Вывод типа переменной
# n = 5
# print(type(n))  # type-запрос, в скобки вставляем саму переменную

# # Способ вывода текста с одной ковычкой
# n = 'fddf'
# print(n)

# n='fd\'fd\'sddffg\'dsggh'
# print(n)

# n = "fdf'ssrsd''gd'sfg"
# print(n)

# # Способ комментирования - #, сотичание ctrl+/ или просто #
# print(5)
# # print(5)
# print(5)

# # Закоментировать кусок кода - """
# """
# print(5, 8)
# print(5)
# print(5, 9)
# """

# # Интерполяция разных типов данных, в строку просто через запятую
# a = 5
# b = 5.89
# c = 'hello'

# print(a, '-', b, '-', c)
# # В {} беруться значения, которые можно вставлять прямо в текст
# print(f'{a} - {b} - {c}')
# # Ещё один вариант
# print('{} - {} - {}'.format(a, b, c))

# # Ввод данных
# print('Введите первую число: ')
# a = input()

# b = input('Введите второе число:  ')
# # в данном случае будет сложение просто строк, не числа
# print(a, '+', b, '=', a + b)
# print(f'{a} + {b} = {a + b}')
# print('{} + {} = {}'.format(a, b, a+b))

# #  Приведение типов
# c = 5.58
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# # Ввод данных с преобразованием
# print('Введите первую число: ')
# a = int(input())
# b = int(input('Введите второе число:  '))
# # в данном случае будет сложение просто строк, не числа
# print(a, '+', b, '=', a + b)
# print(f'{a} + {b} = {a + b}')
# print('{} + {} = {}'.format(a, b, a+b))

# # Округление чисел round
# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))

# # Команды переменной, как пример i++ - приравнивалось к i = i + 1 В С#
# iter = 2
# iter += 3 # iter = iter + 3
# print(iter)
# iter -= 4 # iter = iter - 4
# print(iter)
# iter *= 5 # iter = iter * 5
# print(iter)
# iter /= 5 # iter = iter / 5
# print(iter)
# iter //= 5 # iter = iter // 5
# print(iter)
# iter %= 5 # iter = iter % 5
# print(iter)
# iter **= 5 # iter = iter ** 5
# print(iter)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# Синтаксис
# > Больше
# >= Больше или равно
# < Меньше
# <= Меньше или равно
# == Равно (проверяет, равны ли числа)
# != Не равно (проверяет, не равны ли значения)
# not Не (отрицание)
# and И (конъюнкция)
# or Или (дизъюнкция)

# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# # IF, Else, elif

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# # While
# # Остановка командой break - нежелательно
# i = 0
# while i < 5:
#     # if i == 3: # Способ остановки по достижению числа 3
#     #     break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# # Метод флажка. Находим минимальный делитель числа НОД
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# #  Цикл for. Функция range() всегда шаг
# r = range(5) # 0 1 2 3 4 от 0 до числа, не включая его
# r = range(2, 5) # 2 3 4 с первого числа по второе, не включая его
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9 тут уже 3м числом указали шаг
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80 60 40 20

# # Массивы с for
# a = 'qwerty'
# # print(a[2]) # по примеру массива в данном случае выдаст е
# for i in a:
#     print(i)
    
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# # Определить количество символов в строке:
# print(len(text)) # 39 
# # Проверить наличие символа в строке (in):
# print('ещё' in text) # True
# # Функция, которая делает все буквы строки маленькими:
# print(text.lower()) # съешь ещё этих мягких французских булок 
# # Функция, которая делает все буквы строки большими:
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# # Заменить слово на другое :
# print(text.replace('ещё','БолЬше')) # СъЕШЬ Больше этих МяГкИх французских булок

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок - выводит всё
# print(text[:2]) # съ - выводит нужное колво символов
# print(text[len(text)-2:]) # ок с определенного символа до конца
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)
