# 4. Write a Python program that calculates
# the area of a circle based on the radius entered by the user.


import math


r = float(input("Qual o raio do seu circulo? ").strip())
radius = math.pi*r*r
print(f"A area do seu circulo é: ", round(radius, 2), end=" ")

# Calculo com o diametro

print("\n\nOtimo! Agora vamos calcular com o diametro!")
d = float(input("Qual o diametro do seu circulo? ").strip())
diam = (math.pi*d*d)/4
print("A area do seu circulo é: ", round(diam, 2), end=" ")
