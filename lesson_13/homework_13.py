# ++++++++++++++++++++++++++++++++++++++++++++++++
# Декораторы в Python
# ++++++++++++++++++++++++++++++++++++++++++++++++
# ===============================================
# 1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
# Пример вызова:
# @uppercase_decorator
# def say_hello():
#     return "hello, world!"
# print(say_hello())  # "HELLO, WORLD!"

# def uppercase_decorator(func):   # Принимаем функцию
#     def wrapper(*args, **kwargs):  # Создаем вложенную функцию
#         # Логика ДО вызова
#         result = func(*args, **kwargs)  # Передаем аргументы
#         # Логика после вызова
#         return result.upper()   # Преобразуем результат
#     return wrapper   # Возвращаем новую функцию
# @uppercase_decorator
# def say_hello():
#     return "hello, world!"
# print(say_hello())

# ===============================================
# 2. Создайте декоратор repeat(n), который выполняет функцию n раз.
# Пример вызова:
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()
# Вывод:
# Hello!
# Hello!
# Hello!

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def hello():
#     print("Hello!")
#
# hello()

# ===============================================
# 3. Создайте декоратор cache, который кэширует результаты выполнения функции.
# Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
# Пример вызова:
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
# print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
# print(slow_add(2, 3))  # 5 (результат взят из кэша)

# def cache(func):
#     AB = {}  # создаем пустой словарь для хранения кэша
#     def wrapper(*args):
#         # *args - принимает все позиционные аргументы функции
#         # Например, для slow_add(2, 3) args будет (2, 3)
#
#         if args in AB:      # Проверяем, есть ли уже результат для таких аргументов в кэше
#             return AB[args]   # Если есть - возвращаем сохраненный результат, не вычисляя заново
#         result = func(*args)  # Если результата нет в кэше - вычисляем его
#         AB[args] = result  # Сохраняем результат в кэш под ключом = аргументы
#         return result  # Возвращаем вычисленный результат
#     return wrapper  # Возвращаем функцию-обертку, которая заменит оригинальную функцию
#
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
#
# print(slow_add(2, 3))  # Вычисляю 2 + 3... 5
# print(slow_add(2, 3))  # 5 (берется из кэша)

# ===============================================
# 4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
# Пример вызова:
# @timer(3)
# def slow_function():
#     time.sleep(1)
# slow_function()  # Среднее время выполнения: 1.0002 сек

import time

def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for r in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"Среднее время выполнения: {end_time - start_time} сек")
            return result
        return wrapper
    return decorator
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()