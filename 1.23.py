import math
s = int(input("Enter the length of the side: "))
n = int(input("Enter the number of sides: "))
area = n*(s**2/(4*math.tan(math.pi/n)))
print("Area: " + str(area))
