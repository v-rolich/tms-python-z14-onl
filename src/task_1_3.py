"""
Дана длина ребра куба. Найти объем куба и площадь его боковой
поверхности.
"""

"""
The formula for calculating the volume of a cube
if you only know the length of the edge: V = a ⋅ a ⋅ a = a ** 3
Where 'a' is length of the edge
Where 'volume' is volume of cube
"""

a = 5
volume = a ** 3
print(volume)

"""
The area of the side surface of the cube is equal to the number 
of side faces multiplied by the square of the edge: S = 4 * a ** 2
Where 'square' is side surface area
"""

square = 4 * a ** 2
print(square)
