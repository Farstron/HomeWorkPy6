from functools import reduce
#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

print(*list(filter(lambda x: not 'абв' in x, input(" Введите текст на проверку:\n").split(' '))))

##1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print(sum([int(i) for i in input("Input some number: ") if i.isdigit()]))

# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

lis = [1,2,3,4,5,5]
print('Задание 1: ',reduce(lambda x,y:x+y,[lis[n] for n in range(0,len(lis)) if n%2 == 1]))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = 5
with open('Zadanie5.txt','w') as data:
	data.write(' + '.join([str(str(random.randrange(0,101))+'x^'+str(k-i)) for i in range(0,k+1)])+' = 0')
