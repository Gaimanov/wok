import math

# num = int(input())
# n = 3
# b = (num % 10**n) // 10**(n-1)
# c = (num % 10**(n-1)) // 10**(n-2)
# d = (num % 10**1) // 100
# first = b + c + d
# second = b * c * d
# print(f'Сумма цифр = {first}')
# print(f'Произведение цифр = {second}')
# put your python code here

# num = int(input())
# s = str(num)
# first = int(s[0])
# second = int(s[1]) #Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# third = int(s[2])
# fourth = int(s[-1])
# if first + fourth == second - third:
#     print('Да')
# else: print ('Нет')

# print(min(int(input()),int(input()),int(input()), int(input()))) #min form 4 digits
# a = int(input())
# if a <= 13:
#     print('детство')
# elif a in range(14, 24):
#     print("молодость")
# elif a in range(25, 59):
#     print("зрелость")
# elif a >= 60:
#     print('старость')


# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# a = int(input())
# b = int(input())
# c = int(input())
# if a > 0:
#     b1 = a
# else: b1 = 0
# if b > 0:
#     b2 = b
# else: b2 = 0
# if c > 0:
#     b3 = c
# else: b3 = 0
# print(b1 + b2 + b3)
#
# ILI
# a, b, c = int(input()), int(input()), int(input())
# total = 0
# if a > 0:
#     total = total + a
# if b > 0:
#     total = total + b
# if c > 0:
#     total = total + c
# print(total)

# n = int(input())
# if -30 < n <= -2  or 7 < n <=25:
#     print("Принадлежит")
# else: print("Не принадлежит")

# a = int(input())
# if len(str(a)) == 4 and a % 7 == 0 or a % 17 == 0:
#     print("YES")
# else: print("NO") #невырожденность треугольника

# a = int(input())
# if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
#     print("YES")
# else: print("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == c or b == d:
#     print("YES")
# else: print("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a - c in range(-1, 2) and b - d in range(-1, 2):
#     print("YES")
# else: print("NO")


# a = input()
# b = input()
# print(f'Hello {a}, {b}! You just delved into Python')

# a = input()
# b = input()
# c = input()
# if len(a) > len(b) > len(c):
#     print(b, a, sep='\n')
# elif len(b) > len(a) > len(c):
#     print(a, b, sep='\n')
# elif len(a) > len(c) > len(b):
#     print(c, a, sep='\n')
# elif len(b) > len(c) > len(a):
#     print(c, b, sep='\n')
# elif len(c) > len(a) > len(b):
#     print(a, c, sep='\n')
# elif len(c) > len(b) > len(a):
#     print(b, c, sep='\n')

# put your python code here
# a = input()
# if 'суббота' or 'воскресенье' in a:
#     print('YES')
# else: print('NO')

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# a = int(input())
# for i in range(a):
#     print('*'*19)

# a = input()
# for i in range(10):
#     print(i, a)

# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     print(m * (p / 100 + 1) ** i)

# m = int(input())
# n = int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif n < m:
#     for i in range(m, n-1, -1):
#         print(i)
# elif n == m:
#     print(n)

# m = int(input())
# n = int(input())
# for i in range(m, n):
#     if i % 17 == 0 or (i % 3 == 0 and i % 5 == 0) or i % 10 == 9:
#         print(i)
# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a = int(input())
# b = int(input())
# total = 0
# for i in range(a, b + 1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         total += 1
# print(total)
#
# a = int(input())
# counter = 0
# for i in range(a):
#     m = int(input())
#     counter = counter + m
# print(counter)

# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения 7.3
# total = 1
# n = int(input())
# for i in range(2, n+1):
#     total = total + 1 / i
# over = total - math.log(n)
# print(over)

# n = int(input())
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# total = 1
# for i in range(10):
#     m = int(input())
#     if m != 0:
#         total = total * m
# print(total)

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# a = input()
# while a != 'КОНЕЦ' or a != 'конец':
#     print(a)
#     a = input()

# counter = 0
# a = input()
# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#     counter += 1
#     a = input()
# print(counter)

# RAVNO

# a = 0
# while input() not in ("стоп", "хватит", "достаточно"):
#     a+=1
# print(a)

# a = input()
# while a % 7 == 0:
#     print(a)
#     a = input()

# total = 0
# a = int(input())
# while a >= 0:
#     total += a
#     a = int(input())
# print(total)

# total = 0
# a = int(input())
# while 0 <= a < 6:
#     if a == 5:
#         total += 1
#     a = int(input())
# print(total)

# a = int(input())
# total = a
# coins = 0
# while total >= 25:
#     total -= 25
#     coins += 1
# while total >= 10:
#     total -= 10
#     coins += 1
# while total >= 5:
#     total -= 5
#     coins += 1
# while total >= 1:
#     total -= 1
#     coins += 1
# print(coins)

# n = int(input())
# line = ''
# while n != 0:
#     a = n % 10
#     line += str(a)
#     n = n // 10
# print(line)

# a = int(input())
# b = max(str(a))
# c = min(str(a))
# print(f'Максимальная цифра равна {b}\nМинимальная цифра равна {c}')

# a = int(input())
# sum_all = 0
# colvo_cifer = 0
# proizv = 1
# pervaya = str(a)[0]
# last_number = a % 10
# while a != 0:
#     n = a % 10
#     sum_all += n
#     colvo_cifer += 1
#     proizv *= n
#     a = a // 10
# average = sum_all / colvo_cifer
# summa_dvux = int(pervaya) + last_number
# print(sum_all, colvo_cifer, proizv, average, pervaya, summa_dvux, sep='\n')

# print(str(int(input()))[1])

# a = int(input())
# while len(str(a)) != 2:
#     n = a % 10
#     a = a // 10
# last = a % 10
# print(last)

# n = int(input())
# while n > 99:
#     n //= 10
# print(n % 10)

# PROUD OF 7.4
# a = int(input())
# flag = True
# compare = int(str(a)[0])
# while a != 0:
#     n = a % 10
#     if compare == n:
#         a = a // 10
#     elif compare != n:
#         flag = False
#         a = a // 10
# if flag == True:
#     print("YES")
# elif flag == False:
#     print('NO')

# a = int(input())
# flag = True
# while a != 0:
#     n = int(str(a)[-2])
#     n1 = int(str(a)[-1])
#     if n1 == n or n1 < n:
#         a = a // 10
#     elif n1 != n and n1 > n:
#         flag = False
#         a = a // 10
# if flag == True:
#     print("YES")
# elif flag == False:
#     print('NO')

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# a = int(input())
# for i in range(2, a + 1):
#     if a % i == 0:
#         break
# print(i)

# n, div = int(input()), 2
# while n % div != 0 :
#     div += 1                              GENIUS
# print(div)

# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:           GENIUS-LIKE
#         continue
#     print(i)

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x > 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count, p, sep='\n')
# else:
#     print('NO')

# s = 0
# for i in range(7):
#     n = int(input())
#     if i % 2 == 0:
#         s += n
# print(s)

# n = int(input())
# while len(str(n)) != 1:
#     n = n // 10
# print(n)

# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# ВЛОЖЕННЫЕ ЦИКЛЫ
# # n = int(input())
# # for i in range(1, n + 1):
# #     for i in range(1, 4):
# #         print(n, end=' ')
# #     print()
#
# n = int(input())
# for i in range(1, n+1):
#     for k in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())
# for k in range(1, n + 1):
#     for m in range(1, 10):
#         print(f'{k} + {m} = {k + m}')
#     print()

# n = int(input())
# for i in range(1, n // 2 + 1):
#     for k in range(1, i + 1):
#         print('*', end='')
#     print()
# for i in range(n // 2 + 1, 0, -1):
#     for m in range(1, i + 1):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     print('*' * min(i, n - i + 1))

# n = int(input())
# for i in range(1, n + 1):
#     for k in range(1, i + 1):
#         print(i, end='')
#     print()

# total = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm = ', m)
# print(total)

# n = int(input())
# num = 1
# for i in range(1, n + 1):
#     for k in range(1, i + 1):
#         print(num, end=' ')
#         num += 1
#     print()

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# flag = True
# for i in s:
#     if 'w' in s:
#         flag == True
# print('w')

# n = input()
# for i in range(1, len(n)):
#     print(n[-i])
# print(n[0])

# n = input()
# k = input()
# m = input()
# print(n[0], k[0], m[0], sep='')

# a = int(input())
# total = 0
# for i in str(a):
#     total += int(i)
# print(total)


# SODERZHIT CHTO TO


# n = input()
# flag = False
# for i in n:
#     if i.isdigit():
#         flag = True
#         break
# if flag:
#     print('Цифра')
# else:
#     print('Цифр нет')

# n = input()
# plus = 0
# zvezda = 0
# for i in n:
#     if i in '+':
#         plus += 1
#     if i in '*':
#         zvezda += 1
# print(f'Символ + встречается {plus} раз\nСимвол * встречается {zvezda} раз')

# n = input()
# counter = 0
# sklad = ''
# for i in n:
#     if i == sklad:
#         counter += 1
#     sklad = i
# print(counter)

# s, count = input(), 0
# for i in range(0, len(s)):
#     count += s[i] == s[i-1]
# print(count)

# n = input().lower()
# glas = 0
# soglas = 0
# for i in n:
#     if i in 'ауоыиэяюёе':
#         glas += 1
#     elif i in 'бвгджзйклмнпрстфхцчшщ':
#         soglas +=1
# print(f'Количество гласных букв равно {glas}\nКоличество согласных букв равно {soglas}')
#
# n = int(input())
# b = ''
# while int(n) != 0:                        STUCK
#     b = str(n % 2) + b
#     n = n // 10
# print(b)

# a = input()
# obsh = len(a)
# povt = a + a + a
# perv = a[0]
# perv3 = a[:3]
# posl3 = a[-3:]
# obr = a[::-1]
# udal = a[1:-1]
# print(obsh, povt, perv, perv3, posl3, obr, udal, sep='\n')

# a = input()
# obsh = a[2]
# povt = a[-2]
# perv = a[:5]
# perv3 = a[:-2]
# posl3 = a[::2]
# obr = a[1::2]
# udal = a[::-1]
# odin = a[::-2]
# print(obsh, povt, perv, perv3, posl3, obr, udal, odin, sep='\n')

# a = input()
# x = len(a)//2 + len(a) % 2
# part1 = a[:x]
# part2 = a[x:]
# print(part2 + part1)

# a = input()
# aq = a.title()
# if a ==aq:
#     print('YES')
# else: print('NO')

# a = input().lower()
# if a.__contains__('хорош'):
#     print('YES')
# else:
#     print("NO")

# a = str(input())
# count = 0
# for i in str(a):
#     if i.islower():
#         count += 1
# print(count)

# a = input().lower()
# ad = a.count('а')
# gu = a.count('г')
# ci = a.count('ц')
# ti = a.count('т')
# print(f'Аденин: {ad}\nГуанин: {gu}\nЦитозин: {ci}\nТимин: {ti}')


# n = int(input())
# counter = 0
# for i in range(n):
#     k = input()
#     if k.count('11') and k.count('11') >= 3:
#         counter += 1
# print(counter)

# n = int(input())
# counter = 0
# for i in range(n):
#     k = input()
#     if k.count('11') and k.count('11') >= 3:
#         counter += 1
# print(counter)

# n = input()
# counter = 0
# for i in str(n):
#     if i.isdigit():
#         counter += 1
# print(counter)

# n = input()
# if n.endswith('.com') or n.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# s = input()
# chislo = 0
# stroka = ''
# for i in str(s):
#     if s.count(i) >= chislo:
#         chislo = s.count(i)
#         stroka = i
# print(stroka)
#
# n = input()
# counter = 0
# for i in str(n):
#     if i == 'f':
#         counter += 1
# if counter == 1:
#     print(n.find('f'))
# elif counter >= 2:
#     print(n.find('f'), n.rfind('f'))
# else:
#     print('NO')
#
# s = input()
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") > 1:
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("NO")

# n = input()
# x = n.find('h')
# y = n.rfind('h')
# print(n[:x] + n[y+1:])

# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(chr(i), end=' ')

# n = input()
# code = ''
# for i in str(n):
#     code += str(ord(i))
#     code += str(' ')
# print(code)

# a = int(input())
# b = input().lower
# decode = ''
# for i in str(b):
#     decode += str(ord(i) - 1)
#     decode += str(' ')
# print(decode)
# # for i in decode:

# RABOTA SO SPISKAMI

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# numbers1 = numbers1 * 2
# numbers1 += numbers2 * 9
# numbers1 += numbers3
# print(numbers1)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# del numbers[0]
# del numbers[-1]
# print(numbers)

# n = int(input())
# listok = []
# for i in range(n):
#     a = input()
#     listok.append(a)
# print(listok)

# a = []
# li = 'abcdefghijklmnopqrstuvwxyz'
# umn = 1
# for i in li:
#     a.append(i * umn)
#     umn += 1
# print(a)

# n = int(input())
# li = []
# for i in range(n):
#     a = int(input())
#     li.append(a**3)
# print(li)

# n = int(input())
# li = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         li.append(i)
# print(li)

# n = int(input())
# li = []
# x = []
# for i in range(n):
#     a = int(input())
#     li.append(a)
# for i in range(len(li)-1):
#     x.append(li[i] + li[i+1])
# print(x)

# n = int(input())
# spis1 = []
# for i in range(n):
#     a = int(input())
#     spis1.append(a)
# del spis1[1::2]
# print(spis1)

# PROUD!!11.4

# n = int(input())
# x = []
# y = ''
# for i in range(n):
#     a = input()
#     x.append(a)
# k = int(input())
# for i in x:
#     if k > len(i):
#         continue
#     else:
#         y += i[k-1]
# print(y)

# n = int(input())
# sk = []
# for i in range(n):
#     a = input()
#     sk.extend(a)
# print(sk)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# joke = 0
# for i in numbers:
#     joke += i**2
# print(joke)

# n = int(input())
# k = []
# j = []
# for i in range(n):
#     a = int(input())
#     k.append(a)
#     j.append(a ** 2 + 2*a+1)
# print(*k, sep='\n')
# print()
# print(*j, sep='\n')

# n = int(input())
# k = []
# for i in range(n):
#     a = int(input())
#     k.append(a)
# k.remove(max(k))
# k.remove(min(k))
# print(*k, sep='\n')

# n = int(input())
# lis = []
# for i in range(n):
#     a = input()
#     if a not in lis:
#         lis.append(a)
# print(lis)

# n = int(input())
# li = []
# co = []
# sea = []
# counter = 0
# for i in range(n):
#     a = input()
#     li.append(a)
# k = int(input())
# for i in range(k):
#     search = input()
#     sea.append(i)
#     for i in li:
#         if search.lower() in i.lower():
#             counter += 1
#     if counter == len(sea):
#         co.append(li)
# print(*co, sep='\n')


# SEPARATION/JOIN


# n = input().split()
# a = []
# for i in n:
#     a.append(i[0])
# g = '.'.join(a)
# print(g, end='.')

# n = input()
# g = n.split(' ')
# for i in g:
#     print('+' * int(i))

# n = input()
# g = n.split('.')
# flag = True
# for i in g:
#     if int(i) < 0 or int(i) > 255:
#         flag = False
# if flag == True:
#     print('ДА')
# else:
#     print('НЕТ')
#
# n = input()
# g = input()
# f = g.join(n)
# print(f)

# n = input()
# f = n.split(' ')
# print(f)
# counter = 0
# for i in range(len(f)):
#     for j in (i+1, len(f)):
#         if f[i] == f[j]:
#             counter += 1
# print(counter)

# n = list(input().lower().split())
# a = n.count('a')
# an = n.count('an')
# the = n.count('the')
# su = int(a) + int(an) + int(the)
# print('Общее количество артиклей: ', su)

# n = [int(i) for i in input().split()]
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)

# n = input().split()
# n.sort(key=int)
# print(*n)
# n.sort(reverse=True, key=int)
# print(*n)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [m[0] for m in keywords]
#
# print(new_keywords)

# palindromes = list(range(100, 1001))
# li = []
# for i in palindromes:
#     if str(i) == str(i)[::-1]:
#         li.append(i)
# print(li)
#
# =========
#
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# g = [i ** 2 for i in range(1, int(input()) + 1)]
# print(*g, sep='\n')
# print(*[int(i) ** 3 for i in input().split()])
# print(*[i for i in input().split(' ')], sep='\n')
# print(*[i for i in input() if i.isdigit()], sep='')
# print(*[int(i) ** 2 for i in input() if i % 2 == 0 and i % 10 != 4])


# n = input().split()
# li = []
# for i in n:
#     if int(i) % 2 == 0:
#         i = int(i) ** 2
#         if i % 10 != 4:
#             li.append(i)
# print(*li)


# FUNCTSII

# # объявление функции
# def draw_box():
#     print(10*'*')
#     for i in range(12):
#         print('*        *')
#     print(10*'*')
# # основная программа
# draw_box()  # вызов функции
#
# def draw_box():
#     print(*['*        *' if line not in [0, 13] else '*' * 10 for line in range(14)], sep='\n')
#
#     # основная программа
# draw_box()  # вызов функции

# объявление функции
# counter = 0
# def draw_triangle():
#     for i in range(10):
#         i += 1
#         print('*' * i)
# [i * '*' for i in range(10) i += 1]
# # основная программа
# draw_triangle()  # вызов функции

# объявление функции
# def draw_triangle(fill, base):
#     count = 0
#     step = 1
#     for _ in range(base):
#         if count == base//2 + 1:
#             step = -1
#         count += step
#         print(fill * count)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# объявление функции
# def print_fio(name, surname, patronymic):
#     u = ''
#     g = surname, name, patronymic
#     for i in g:
#         u += i[0]
#     print(u, sep='')
# # считываем данные
# name, surname, patronymic = input().upper(), input().upper(), input().upper()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# # объявление функции
# def print_digit_sum(num):
#     sum = 0
#     while num != 0:
#         a = num % 10
#         sum += int(a)
#         num = num // 10
#     print(sum)
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)

# объявление функции
# def is_prime(num):
#     counter = []
#     for i in range(1, num  + 2):
#         if num % i == 0:
#             counter.append(i)
#     if len(counter) == 2:
#         return True
#     else:
#         return False


# DIFFICULT PROBLEM

# def is_prime(num):
#     counter = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter.append(i)
#     if len(counter) == 2:
#         return True
#     else:
#         return False
#
# def get_next_prime(num):
#     j = num + 1
#     while not is_prime(j):
#         j += 1
#     return j
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))

# объявление функции
# def is_password_good(password):
#     flag = False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     if len(password) >= 8:
#         flag = True
#     for i in password:
#         if i.isupper():
#             flag1 = True
#     for j in password:
#         if j.islower():
#             flag2 = True
#     for k in password:
#         if k.isdigit():
#             flag3 = True
#     if flag == True and flag1 == True and flag2 == True and flag3 == True:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))

# # объявление функции
# def is_one_away(word1, word2):
#     flag1 = False
#     flag2 = False
#     flag3 = True
#     counter = 0
#     if len(word1) == len(word2):
#         flag1 = True
#     for i in range(0, len(word1)):
#         if word1[i] == word2[i]:
#             counter += 1
#     if len(word1) - counter == 1:
#         flag2 = True
#     if word1 == word2:
#         flag3 = False
#     if flag1 == True and flag2 == True and flag3 == True:
#         return True
#     else:
#         return False
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

# объявление функции
# def is_palindrome(text):
#     li = []
#     for i in text.lower():
#         if i not in(',', '.', ' ', '!', '?', '-'):
#             li.append(i)
#     if li == li[::-1]:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))

# # объявление функции
# def is_valid_password(password):
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     password = list(password.split(':'))
#     if len(password) > 3:
#         return False
#     if password[0] == password[0][::-1]:
#             flag1 = True
#     counter = []
#     for i in range(1, int(password[1]) + 1):
#         if int(password[1]) % i == 0:
#             counter.append(i)
#     if len(counter) == 2:
#         flag2 = True
#     if int(password[2]) % 2 == 0:
#         flag3 = True
#     if flag1 == True and flag2 == True and flag3 == True:
#         return True
#     else:
#         return False
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

# объявление функции
# def is_correct_bracket(text):
#     counter = 0
#     for i in text:
#         if i == '(':
#             counter += 1
#         if i == ')':
#             counter -= 1
#         if counter < 0:
#             return False
#     if counter == 0:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# объявление функции
# def convert_to_python_case(text):
#     result = text[0].lower()
#     for i in text[1:]:
#         if i.isupper():
#             result += '_' + i.lower()
#         else:
#             result += i
#     return result
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))

# # объявление функции
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         k = (-b + math.sqrt(b**2-4*a*c)) / 2*a
#         m = (-b - math.sqrt(b**2-4*a*c)) / 2*a
#         return k,m
#     if d == 0:
#         x1 = -(b / 2*a)
#         x2 = -(b / 2*a)
#         return x1, x2
#     if d < 0:
#         return d, d
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# n = int(input())
# li = []
# for i in range(n):
#     a = int(input())
#     li.append(a)
# li.sort()
# print(li[-1])
# li.pop(-1)
# print(li[-1])

# n = int(input())
# li = [0, 1]
# for i in range(n):
#     li.append(li[-2]+li[-1])
#     i += 1
# li.pop(-1)
# li.pop(0)
# print(*li)

# n = input()
# counter = 0
# for i in n:
#     if i == 'f':
#         counter += 1
# if counter == 0:
#     print('-2')
# elif counter == 1:
#     print('-1')
# else:
#     print(n.replace('f', 'g', 1).find('f'))

# n = input()
# f = n.find('h')
# k = n.rfind('h')
# print(n[:f]+n[k:f:-1]+n[k:])

# n = int(input())
# lis = []
# for i in range(1 ,n+1):
#     if i % 2 == 0:
#         lis.append(i)
# print(lis)

# lst_1 = [int(i) for i in input().split()]
# lst_2 = [int(i) for i in input().split()]
# lis = []
# for i in range(len(lst_1)):
#     lis.append(int(lst_1[i])+int(lst_2[i]))
# print(*lis)

# n = input().split()
# lis = 0
# lis1 = ''
# for i in n:
#     lis += int(i)
# print(*n, sep='+', end='='+ str(lis))

# n = input().split()
# big = 0
# for i in n:
#     if len(i) > big:
#         big = len(i)
# print(big)
#
# # объявление функции
# def get_shipping_cost(quantity):
#     quan = quantity - 1
#     if quantity >= 2:
#         return 1000 + 125 * quan
#     else:
#         return 1000
#
# # считываем данные
# n = int(input())

# вызываем функцию
# print(get_shipping_cost(n))

# import math
# def compute_binom(n, k):
#     n1 = math.factorial(n)
#     k1 = math.factorial(k)
#     k2 = math.factorial(k1*(n-k))
#     res = n1 / k2
#     return int(res)
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))

# объявление функции
# def is_pangram(text):
#     flag = True
#     slovo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in slovo:
#         if i not in text.lower():
#             flag = False
#     if flag == True:
#         return True
#     else:
#         return False
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))
































































