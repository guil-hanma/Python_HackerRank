# 6. Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers.


import numpy as np

valores = input("Insira os valores separados por virgula: ")
list = valores.split(","),
# Mudança de str>int feita usando a biblioteca Numpy
np.array(list, dtype=int)

#  Passa os valores recebidos para int
# list = [int(valores.strip()) for valores in list]
tuple = tuple(list)
print(f"Sua lista é: {list}, \nSeu tuple é: {tuple}")
