import math
a = int(input("Enter the length of first side: "))
b = int(input("Enter the length of second side: "))
c = int(input("Enter the length of third side: "))
s = (a + b + c)/2
area = math.sqrt(s*(s - a)*(s - b)*(s - c))
print("The area of triangle: " + str(area))