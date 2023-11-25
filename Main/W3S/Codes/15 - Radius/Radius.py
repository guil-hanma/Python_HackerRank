# A sphere is a three-dimensional solid with no face, no edge, no base and no vertex. It is a round body with all points on its surface equidistant from the center. The volume of a sphere is measured in cubic units.
# The volume of the sphere is : V = 4/3 × π × r3 = π × d3/6.

# calculando o volume de uma esfera
import math

r = float(input("Qual o raio da sua esfera? ").strip())
volume = (4*math.pi*r*r*r)/3
print(f"O volume da sua esfera é: ", round(volume, 2), end=" ")
