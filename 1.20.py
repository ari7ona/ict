p = int(input("Enter pressure: "))
v = int(input('Enter volume: '))
t = int(input('Enter temperature: '))
r = 8.314
n = (p*v)/(r*t)
print("Number of moles: " + str(n))
