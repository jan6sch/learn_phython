import math

radius = float(input("What is the radius of the circle?: "))

# result = math.pi * (radius ** 2)
result = math.pi * pow(radius, 2)

print(round(result, 2))