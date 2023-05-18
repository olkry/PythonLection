# def f(x):
#     return x * x
#
# print(f(5))
# print(type(f))
# a = f
# print(a(5))
# print(type(a))

# def calk1(a, b):
#     return a + b
#
# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk1, 5, 45)
# math(calk2, 5, 45)

# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# calk1 = lambda a, b: a + b
#
# # math(calk1, 5, 45)
# # math(calk2, 5, 45)
#
# math(lambda a, b: a + b, 5, 45)

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# # Стандартный способ:
# for i in data:
#     if i % 2 ==0:
#         res.append((i, i**2))
# print(res)

# #Через лямбда функции:
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x %2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# Перепишем код используя map и filter

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x %2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# # Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# # возвращает итератор с новыми объектами.
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

# data = '15 156 96 3 5 8 52 5'
# # print(data)
# #
# # data = data.split()
# # print(data)
#
# data = list(map(int, data.split()))
# print(data)

# Функция filter

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# # Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# # из элементов входных данных
#
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)
#
# # Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.

# Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data)