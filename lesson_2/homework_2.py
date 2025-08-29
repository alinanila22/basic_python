# ++++++++++++++++++++++++++++++++++++++++++++++++
# "Числа и арифметические операции"
# ++++++++++++++++++++++++++++++++++++++++++++++++
# ================================================
# 1. Работа с целыми и вещественными числами
# ===================================

a = 8
b = 3
x = 2.5
y = -1.7
print(type(a))
print(type(b))
print(type(x))
print(type(y))

# ================================================
# 2. Основные арифметические операции
# ================================================

num1 = 10
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

# ================================================
# 3. Особенности работы с делением
# ================================================

a = 10
b = 3
print(a / b)
print(a // b)
print(a % b)

a = -10
b = 3
print(a / b)
print(a // b)
print(a % b)

a = 10
b = -3
print(a / b)
print(a // b)
print(a % b)

# ================================================
# 4. Работа с приоритетом операторов
# ================================================

print(5 + 3 * 2) #сначала умножение, а потом сложение
print((5 + 3) * 2) #сначала сложение в скобке, а потом умножение
print(10 / 2 ** 2) #сначала возведение в степень в знаменателе, а потом деление

# ================================================
# 5. Использование сокращенных операторов
# ================================================

count = 10
count += 5 # count = count + 5
count -= 3 # count = count - 3
count *= 2 # count = count * 2
count /= 4 # count = count / 4
print(count) # итоговое значение count = 6.0


# ++++++++++++++++++++++++++++++++++++++++++++++++
# "Строки в Python".
# ++++++++++++++++++++++++++++++++++++++++++++++++
# ================================================
# 1. Создание строк
# ================================================

s1 = "Python"
s2 = 'Программирование'
print(s1)
print(s2)

npr_interview_highlights = '''
In 'The Roses,' Benedict Cumberbatch and Olivia Colman play a couple at odds
Many movies that have been made detail the start of relationships.

Those dizzying first moments of love — flirtation and the spark of attraction, first kisses and the will-they-or-won't-they tension of so many romantic comedies.
But what about a film centered on the other end of love, when things fall spectacularly apart? That's what we see play out in the new dark comedy, The Roses, starring Benedict Cumberbatch and Olivia Colman. They play husband and wife, Theo and Ivy, an architect and chef, respectively. They are a couple who were once very much in love, but now — two children and one transatlantic move later — are facing the possible demise of their marriage.
'''
print(npr_interview_highlights)

empty = ""
print(len(empty))

# ================================================
# 2. Конкатенация строк
# ================================================

first_name = "Иван"
last_name = "Петров"

full_name = first_name + ' ' + last_name
print(full_name)

# ================================================
# 3. Преобразование типов
# ================================================

s = "Возраст: "
age = 25
result = s + str(age)
print(result)

# ================================================
# 4. Дублирование строк
# ================================================

s3 = ("xa ") * 5
print(s3)

# s2 = ("xa ") * 2.5
# print(s2)  #Ошибка при умножении на 2.5: can't multiply sequence by non-int of type 'float'

# ================================================
# 5. Длина строки
# ================================================

text = "Привет, мир!"
print(text)
print(len(text))

s4 = "  "
print(s4)
print(len(s4)) # в кавычках находится 2 пробела

# ================================================
# 6. Проверка вхождения подстроки
# ================================================

sentence = "Я изучаю Python"
print("Python" in sentence) #True
print("Java" in sentence) #False

# ================================================
# 7. Сравнение строк
# ================================================

a = "apple"
b = "banana"
print(a == b) #Falsу
print(a != b) #True
print(a < b) #True
print(a > b) #False
print(a <= b) #True
print(a >= b) #False

# ================================================
# 8. Код символов
# ================================================

print(ord('A')) #Код символа 'A'=65
print(ord('a')) #Код символа 'a'=97
print(ord('Я')) #Код символа 'Я'=1071


