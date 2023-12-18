"""✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов."""
# import time
#
# start = time.time()
#
#
# sp = int(input()).split()
# print(sp)
# result = []
# for i in sp:
#
#     if sp.count(i) > 1:
#
#         result.append(i)
#
# print(list(set(result)))
# end = time.time()
# print(end-start)

"""В большой текстовой строке text подсчитать количество встречаемых слов
и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов."""
# text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# text = text.lower()
#
# words = ''
# punc = ",.!#$:()'~@%;?"
# for i in text:
#     if i.isdigit():
#         words += ''
#     elif i not in punc:
#         words += i
#     elif i == "'":
#         words += ' '
#
#
# print(words.replace('-', ' '))
#

'''На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.

Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}.

Достаточно вернуть один допустимый вариант.'''
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

backpack = {}
for k, v in items.items():
    if max_weight - v >= 0:
        backpack[k] = v
        max_weight -= v

print(backpack)