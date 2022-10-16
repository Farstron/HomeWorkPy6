from functools import reduce

# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

lis = [1,2,3,4,5,6]
print('Задание 1: ',reduce(lambda x,y:x+y,[lis[n] for n in lis if n%2 == 1]))

# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

lis1 = [1.1,2.2,3.001,4.4]
lis2 = [round(lis1[n] - round(lis1[n]),10) for n in range(0,len(lis1))]
print('Задание 2: ', max(lis2)-min(lis2))

# Задайте список из n чисел последовательности f и выведите на экран их сумму.

n = 6
f = round((1+1/n)**n)
d = {x: f*x+1 for x in range(1, n+1)}
print(f'Задание 3: для {n = }: {d}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(k,fib_lis=[0,1],pos=1):
    if k!=1:
        fib_lis.append(fib_lis[pos-1]-fib_lis[pos])
        return fib(k-1,fib_lis,pos+1)
    fib_lis.reverse()
    fib_lis.extend([abs(fib_lis[i]) for i in range(len(fib_lis)-2,-1,-1)])
    return fib_lis
print('Задание 4: ',fib(8))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = 5
with open('Zadanie5.txt','w') as data:
	data.write(' + '.join([str(str(random.randrange(0,101))+'x^'+str(k-i)) for i in range(0,k+1)])+' = 0')