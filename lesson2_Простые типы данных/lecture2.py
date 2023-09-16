# a = 5
# print(type(a))
#
# data = 3.14
# print(isinstance(data, (int, float, complex)))
#
# num = 2 + 2 * 2
# digit = 36 / 6
# print(num == digit)
# print(num is digit)
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))
#
# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))
#
# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))

#

# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(hash(my_list))
#
# txt = input()
# print(type(txt), id(txt), hash(txt))

# a: int | float = 42
# b: float = float(input('Введи число: '))
# a = a / b
#
#
# def my_func(data: list[int, float]) -> float:
#     res = sum(data) / len(data)
#     return res
#
#
# print(my_func([2, 5.5, 15, 8.0, 13.74]))

#
# print("Hello world!".__doc__)
# print(str.__doc__)

# print("Hello world!".upper())
# print("Hello world!".count('l'))
#
# print(dir("Hello world!"))
#
# help("Hello world!")

# help()
#
# x = int("42")
# y = int(3.1415)
# z = int("hello", base=36)
# print(x, y, z, sep='\n')
#
# import sys
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP

# num = 7_901_123_456_789
# print(num)
#
# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)

# print(0.1 + 0.2)
#
# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi)
#
#
# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения по умолчанию: '))
# level = num or DEFAULT
# print(level)


# name = input('Как вас зовут? ')
# if name:
#     print('Привет, ' + name)
# else:
#     print('Анонимус, приветствую')

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# while data:
#     print(data.pop())

# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
#         " до ста лет, но длина строки не должна превышать " +\
#         str(LIMIT) + ' символов.'
# print(text)


# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())


import math
#
# print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
# print(dir(math))
# print(help(math.gcd))

import decimal, fractions
# print(0.1 + 0.2)
#
# pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)
#
#
# decimal.getcontext().prec = 120
# science = 2 * pi * decimal.Decimal(23.452346) ** 2
# print(science)
#
# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)
#
#
# a = complex(2, 3)
# b = complex('2+3j')
# print(a, b, a == b, sep='\n')

print(pow(2,4,3))