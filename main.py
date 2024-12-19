#Написать программу, которая:

#- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка  **[-15, -4, -2, -7, 0, 3, 5, 12, 7]**

#- Выводит данную матрицу в форматированном виде.

import random
values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]
height = random.randint(4,8)
width = random.randint(4,8)
#Составление матрицы
matrix =[[random.choice(values) for i in range(width)] for k in range(height)] 
for arr in matrix:
    for num in arr:
        print(num,end=" ")
    print()
sum = 0
for i in matrix:
    for k in i:
        if k%2!=0:
         sum+=k
print("Сумма нечетных чисел:",sum)
