# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint

# n = int(input("Enter the number of coins"))

# tails = 0
# eagle = 0

# for i in range(n):
#     temp = randint(0, 1)
#     print(temp)
#     if temp > 0: tails += 1
#     else: eagle += 1

# if tails > eagle:
#     print(f'Need to flip  {eagle} coins')
# else:
#     print(f'Need to flip {tails} coins')



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Введите сумму чисел: '))
# p = int(input('Введите произведение: '))

# x = 0
# y = 0

# for i in range(s):
#     for j in range(s):
#         if i + j == s and i * j == p:
#             if i <=1000 and j<=1000:
#                 x = i
#                 y = j
#             else:
#                 print('Введены не верные данные!')

# print(f'X = {x} Y = {y}')



# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Enter number: "))
# m = 1
# while m < n:
#     print(m)
#     m = m * 2






            
            
            













