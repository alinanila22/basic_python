# ++++++++++++++++++++++++++++++++++++++++++++++++
# Лямбда-функции
# ++++++++++++++++++++++++++++++++++++++++++++++++
# ===============================================
# 1. Создайте lambda-функцию, которая возвращает квадрат числа.

# num1 =lambda x: x**2
# print(num1(4))
#
# Пример:
# 16
# ===============================================
# 2. Создайте lambda-функцию, которая проверяет, является ли число четным.

# num = lambda x: x % 2 == 0
# print(num(2))  #True
# print(num(11))  #False
# print(num(-6))  #True
# print(num(-7))  #False

# ===============================================
# 3. Используйте lambda в sorted(), чтобы отсортировать список строк по последней букве.
# Пример вызова:
# words = ["banana", "apple", "cherry"]- лучше указать в другой последовательности: ["cherry","banana", "apple"],чтобы отсортировать по последней букве!
# print(sort_by_last_letter(words))
# Ожидаемый результат:
# ['banana', 'apple', 'cherry']

# def sort_by_last_letter(words):
#     return sorted(words, key=lambda x: x[-1])
# words = ["cherry","banana", "apple"]
# print(sort_by_last_letter(words))

# Пример:
# ['banana', 'apple', 'cherry']- как раз по алфавиту последних букв произошла сортировка
# Порядок сортировки по ASCII кодам(по возрастанию):
# 97 (a) < 101 (e) < 121 (y) → ['banana', 'apple', 'cherry']

# ===============================================
# ++++++++++++++++++++++++++++++++++++++++++++++++
# Замыкания
# ++++++++++++++++++++++++++++++++++++++++++++++++
# 1. Создайте функцию multiply_by(n), которая принимает число n и возвращает вложенную функцию.
# Вложенная функция должна принимать число x и возвращать его произведение на n.
# Пример вызова:
# times3 = multiply_by(3)
# times5 = multiply_by(5)

# print(times3(10))  # 30
# print(times5(10))  # 50

# def multiply_by(n):
#     def multiply_x(x):
#         return x * n
#     return multiply_x
#
# times3 = multiply_by(3)
# times5 = multiply_by(5)
#
# print(times3(10))
# print(times5(10))
# ++++++++++++++++++++++++++++++++++++++++++++++++
# 2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
# Каждый вызов вложенной функции должен увеличивать счетчик на 1.
# Пример вызова:
#
# c1 = counter(5)
# c2 = counter()
#
# print(c1())  # 6
# print(c1())  # 7
# print(c2())  # 1
# print(c2())  # 2
#
# Подсказка: используйте nonlocal

# def counter(start=0):
#     count = start
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
# c1 = counter(5)
# c2 = counter()
# print(c1())  # 6
# print(c1())  # 7
# print(c2())  # 1
# print(c2())  # 2