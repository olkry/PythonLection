# СПИСКИ

# list_1 = []  # создать пустой список
# list_2 = list()  # аналогично
# list_3 = [1, 2, 3, 8]  # вручную заполненый список
# print(list_1)
# print(list_2)
# print(list_3)
# print(*list_3)  # * удалит все знаки, скобки, запятые

# for i in list_3:  # вывод всех элементов списка циклом
#     print(i)

# print(len(list_3))  # выведет размер списка

# print(list_3[3])  # поэлементное выведение списка от 0

# print(list_3[-2])  #поэлементное выведение списка с конца

# Добовление значений в список

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)  # Добовляет в конец указанный символ
# print(list_1)
# list_1.append(85)  # Добовляет в конец указанный символ
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# list_1.insert(2, 11)
# list_1.insert(len(list_1) - 1, 5)
# print(list_1)  # [12, 7, 11, -1, 21, 5, 0]
#
# a = list_1.pop()
# print(a)
# print(list_1)
# print(list_1.pop(1))
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])  # 1
# print(list_1[1])  # 2
# print(list_1[len(list_1) - 1])  # 10
# print(list_1[-5])  # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])  # [1, 2]
# print(list_1[len(list_1) - 2:])  # [9, 10]
# print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])  # []
# print(list_1[0:len(list_1):6])  # [1, 7]
# print(list_1[::6])  # [1, 7]

# Кортеж - неизменяемый список

# t = ()  # Создание пустого кортежа
# print(type(t))
#
# t = (1, 5, 3,)  # Создание кортежа с числом (,) - запятая обязательно в конце
# print(type(t))

# v = [2, 4, 6]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))
#
# c, b, a = v
# print(a,c,b)

# t = (1, 2, 3, 5, 9)
# print(t)
# # for i in t:
# #     print(i)
# # for i in range(len(t)):
# #     print(t[i])
# t[0] = 2  # Tuple не поддерживает преобразование документов.

# Словари - неупорядоченные коллекции с доступом по ключу.

# d = {}  # Создание пустого словоря
# d = dict()  # Создание пустого словоря
# d['q'] = 'qwerty'  # По ключу q получаем qwerty
# print(d)
# d['w'] = 'water'
# print(d)
# print(d['w'])  # Выводит значение по ключу

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться
# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']  # удаление элемента
# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# МНОЖЕСТВА - содержат в себе уникальные элементы, не обязательно упорядоченные

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}  - копия с а
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}  - обьединение а с b
# i = a.intersection(b)  # i = {8, 2, 5}  - пересечения в a с b
# dl = a.difference(b)  # dl = {1, 3} - разность, из a вычли b
# dr = b.difference(a)  # dr = {13, 21} - разность, из b вычли a
# q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# List comprehension — это упрощенный подход к созданию списка, который задействует цикл for
# , а также инструкции if-else для определения того, что в итоге окажется в финальном списке.

# Создаём список чисел от 1 до 100
# list_1 =[]
# for i in range(1,101):
#     list_1.append(i)
# print(list_1)

# Запишем проще
# list_1 = [i for i in range(1, 101)]
# print(*list_1)

# Добавим условия (только четные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(*list_1)

# Решили создать пары каждым четным числам (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(*list_1)

# Можем также сразу и умножать значение, например на 3
# list_1 = [i * 3 for i in range(13) if i % 2 == 0]
# print(list_1)

# ОШИБКИ!!!

# # SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!!
# print(number_first)
# # Отсутствие :

# # IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов

# # TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# # ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

# # KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# # NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует

# # ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения