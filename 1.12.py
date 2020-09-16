import math
t1 = float(input("Enter the latitude of the first point: "))
g1 = float(input("Enter the longitude of the first point: "))
t2 = float(input("Enter the latitude of the second point: "))
g2 = float(input("Enter the longitude of the second point: "))
distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("The distance between two point is " + str(distance) + " kilometers")
