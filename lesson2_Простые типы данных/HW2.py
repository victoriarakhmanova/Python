# Задание №1
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
#

#
# def show_balance(balance):
#     print(f'Ваш баланс {balance} у.е.')
#
#
# def commission(money, percent_take_off):
#     percent = money * percent_take_off
#     if percent < 30:
#         print(f'Комиссия за снятие 30 у.е.')
#         return 30
#     elif percent > 600:
#         print(f'Комиссия за снятие 600 у.е.')
#         return 600
#     else:
#         print(f'Комиссия за снятие {percent} у.е.')
#
#         return percent
#
#
# def wealth_tax(money, balance):
#     tax = money * 0.1
#     if balance > 5000000:
#         balance -= tax
#         print(f'Ваш баланс превысил лимит, поэтому вам начислен налог в размере {tax} у.е.')
#         print(f'Теперь ваш баланс {round(balance, 2)} у.е.')
#         return balance
#
#
# def add(balance):
#     money = int(input('Введите сумму для пополненеия кратно 50 у.е.: '))
#     if money % 50 != 0:
#         print("Мы не можем зачислить эту сумму, она не кратна 50.")
#         return balance
#     balance += money
#     if balance > 5000000:
#         balance = wealth_tax(money, balance)
#         return balance
#     show_balance(balance)
#
#     return balance
#
#
# def take_off(balance):
#     money = int(input('Введите сумму для снятия кратно 50 у.е.: '))
#     if money % 50 != 0:
#         print("Вы не можете снять эту сумму, она не кратна 50.")
#         return balance
#     if money > balance:
#         print('У вас недостаточно средств')
#         return balance
#     if balance == money:
#         print(f'У вас недостаточно средств, вам доступно {money - commission(money, 0.015)} ')
#
#         return balance
#     if balance > 5000000:
#         balance = wealth_tax(money, balance)
#         balance -= (money + commission(money, 0.015))
#         show_balance(balance)
#         return balance
#     else:
#         balance -= money + commission(money, 0.015)
#         show_balance(balance)
#         return balance
#
#
#
#
# def menu_of_atm():
#     balance = 0
#     count_action = 0
#
#     while True:
#         print('Операции: \n        0. Баланс \n        1. Пополнить \n        2. Снять \n        3. Выйти')
#         action = input('Пожалуйста введите действие, которое вы хотите осуществить:  ')
#         if action == '1':
#             balance = add(balance)
#             count_action += 1
#         elif action == '2':
#             balance = take_off(balance)
#             count_action += 1
#         elif action == '0':
#             show_balance(balance)
#         elif action == '3':
#             print('До свидания.')
#             quit()
#         else:
#             print('Неверный ввод, попробуйте ещё')
#
#         if count_action % 3 == 0:
#             print(f'Вам начислен бонус {round(balance * 0.03, 2)} у.е.')
#             balance += round((balance * 0.03), 2)
#             print(f'Теперь ваш баланс {round(balance, 2)} у.е.')
#
#
#
# menu_of_atm()
#
# задание 2
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

BIN = 2
OCT = 8
HEX = 16
num = int(input('Введите число: '))

for div in [BIN, OCT, HEX]:
    test_num = num
    result = ''
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div
    print(f'For {div} {result = }')

# Задание 3
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
#

#
# s1, s2 = input('Введите дробь: '), input('Введите дробь: ')
# l1, l2 = s1.split('/'), s2.split('/')
#
# num1, den1 = int(l1[0]), int(l1[1])
# num2, den2 = int(l2[0]), int(l2[1])
#
# print(num1,den1, num2, den2)
#
#
# if den1 > den2:
#     maxim = den1
# else:
#     maxim = den2
# while True:
#     if ((maxim % den1 == 0) and (maxim % den2 == 0)):
#         nok = maxim
#         break
#     maxim += 1
# if den1 == den2:
#     print(f'Сумма дробей {s1} + {s2} = {(num1 + num2)}/{den2}')
# print(nok)
#
# total = int(((nok/den1)*num1) + ((nok/den2)*num2))
# print(total)
# for i in range(1, min(total, nok) + 1):
#     if total % i == 0 and nok % i == 0:
#         div = i
#
# print(f'Сумма {s1} + {s2} = {int(total/div)}/{int(nok/div)}')
#
# mult1 = num1 * num2
# mult2 = den1 * den2
#
# for i in range(1, min(mult1, mult2) + 1):
#     if mult1 % i == 0 and mult2 % i == 0:
#         d = i
#
# print(f'Произведение {s1} * {s2} = {int(mult1/d)}/{int(mult2/d)}')
#
# from fractions import Fraction
# num1 = Fraction(35, 72)
# num2 = Fraction(45, 115)
# print(num2+num1, num1*num2)