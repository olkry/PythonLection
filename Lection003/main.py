# # Создание функции сумирующей числа и выводящую его
# def sum_numbers(n):
#     summa = 0
#     for i in range(1,n+1):
#         summa += i
#     print(summa)
# sum_numbers(5)

# # Создание функции сумирующей числа и возврощающей переменную
# def sum_numbers(n):
#     summa = 0
#     for i in range(1,n+1):
#         summa += i
#     return summa
#
# print(sum_numbers(10))
#
# a = sum_numbers(5)
# print(a)

# # А теперь с приёмкой и выводом текста
# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1,n+1):
#         summa += i
#     return summa
# a = sum_numbers(5, 'qwerty')
# print(a)

# # Функция принимающая неограниченное кол-во аргументов
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
#
#
# print(sum_str('q', 'w', 'r'))
# print(sum_str('q', 'w', 'r', 'p', 't'))
# # print(int(sum_str(1, 8, 4)))

# Импорт функции из проекта
# import modul1
#
# print(modul1.maxl(5, 9))

# # Перенос функции в проект
# from modul1 import maxl  # Вместо конкретной функции можно поставить *,
#                         # тогда импортируются все функции
# print(maxl(4, 6))

# # Импорт модуля с переименованием
# import modul1 as m1
#
# print(m1.maxl(5, 9))

# # РЕКУРСИЯ с числом Фибоначчи
# p = int(input('ss'))
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# list_1 = []
# for i in range(1, p + 1):
#     list_1.append(fib(i))
# print(list_1)
#
# print(fib(p))

# # Алгоритм быстрой сортировки
#
# def quick_sort(arrey):
#     if len(arrey) <= 1:
#         return arrey
#     else:
#         pivot = arrey[0]
#     less = [i for i in arrey[1:] if i <= pivot]
#     greater = [i for i in arrey[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
#
# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))

# Сортировка слияния
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        right = nums[mid:]
        left = nums[:mid]
        merge_sort(right)
        merge_sort(left)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list_1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list_1)
print(list_1)
