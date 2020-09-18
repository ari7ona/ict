#ex1
print("Name: Akhan")
print("E-mail: skyexline@gmail.com")

#ex2
print("Enter your name:")
x = input()
print("Hello, " + x)

#ex3
x = float(input("Enter the width: "))
y = float(input("Enter the length: "))
z = float(x * y)
print("The area: " + str(z))

#ex4
x = float(input("Enter the width(in feet): "))
y = float(input("Enter the length(in feet): "))
z = float((x * y)/43560)
print("The area: " + str(z) + " acres")

#ex5
s_c = int(input("Enter the number of small containers: "))
l_c = int(input("Enter the number of large containers: "))
refund = (s_c * 0.10) + (l_c * 0.25)
print("Your refund is $" + "{0:.2f}".format(float(refund)))

#ex6
charge = float(input("Enter you charge of the food: "))
tip = 0.18 * charge
tax = 0.10 * charge
total = charge + tip + tax
print("Charge: $" + "{0:.2f}".format(float(charge)), "Tip: $" + "{0:.2f}".format(float(tip)), "Tax: $" + "{0:.2f}".format(float(tax)), "Total: $" + "{0:.2f}".format(float(total)))

#ex7
n = int(input("Enter a number: "))
sum_num = (n * (n + 1)) / 2
print(sum_num)

#ex8
x = int(input("Enter the number of widgets: "))
y = int(input("Enter the number of gizmos: "))
z = 75 * x + 112 * y
print("Total weight: " + str(z))

#ex9
x = int(input("Enter the amount of money: "))
y = x * 0.04
print("After one year you'll have: " + str(x + y), "After two years you'll have: " + str(x + 2*y), "After three yearrs you'll have: " + str(x + 3*y))

#ex10
import math
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
sum = x + y
diff = x - y
prod = x * y
quot = x / y
rem = x % y
lag = math.log10(x)
print("Sum: " + str(sum), "Diff:" + str(diff), "Prod: " + str(prod), "Quot: " + str(quot), "Rem: " + str(rem), "Log: " + str(lag))

#ex11
x = int(input("Enter MPG: "))
y = x * 282.48
print("Your amount of MPG is equal to " + str(y) + " liters per 100 km")

#ex12
import math
t1 = float(input("Enter the latitude of the first point: "))
g1 = float(input("Enter the longitude of the first point: "))
t2 = float(input("Enter the latitude of the second point: "))
g2 = float(input("Enter the longitude of the second point: "))
distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("The distance between two point is " + str(distance) + " kilometers")

#ex13
x = int(input("Enter price: "))
while x > 0:
    if x >= 200:
        print("200 ")
        x -= 200
    elif x >= 100 and x < 200:
        print("100 ")
        x -= 100
    elif x >= 50 and x < 100:
        print("50 ")
        x -= 50
    elif x >= 25 and x < 50:
        print("25 ")
        x -= 25
    elif x >= 10 and x < 25:
        print("10 ")
        x -= 10
    elif x >= 5 and x < 10:
        print("5 ")
        x -= 5
    elif x >= 1 and x < 5:
        print("1 ")
        x -= 1

#ex14
x = int(input("Enter feet: "))
y = int(input("Enter inches: "))
z = (y + x*12)*2.54
print("Your height is " + str(z) + "centimeters")

#ex15
x = int(input("Enter feet: "))
y = x*12
z = x*0.33
w = x*0.00019
print(str(x) + " feet" + " in inches: " + str(y), " in yards: " + str(z), " in miles: " + str(w))

#ex16
import math
r = int(input("Enter the radius: "))
area = math.pi*r**2
volume = 4/3*math.pi*r**3
print("The area: " + str(area), "The volume: " + str(volume))

#ex17
m,t = map(int,input("Mass and temperature").split())
c = 4.186
q = m*c*t
CentPerKw = 8.9
print("q =",q,"J\nCost of boiling water:",q*CentPerKw/(60*60))

#ex18
import math
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
volume = (math.pi*r**2)*h
print("Volume of cylinder: " + str(volume))

#ex19
import math
h = int(input("Enter the height"))
vi = 0
g = 9.8
vf = vi**2 + 2*g*h
print("Final velocity is: " + str((math.sqrt(vf))))

#ex20
p = int(input("Enter pressure: "))
v = int(input('Enter volume: '))
t = int(input('Enter temperature: '))
r = 8.314
n = (p*v)/(r*t)
print("Number of moles: " + str(n))

#ex21
b = int(input("Enter the base of triangle: "))
h = int(input("Enter the height of triangle: "))
area = b * (h/2)
print("Area of triangle: " + str(area))

#ex22
import math
a = int(input("Enter the length of first side: "))
b = int(input("Enter the length of second side: "))
c = int(input("Enter the length of third side: "))
s = (a + b + c)/2
area = math.sqrt(s*(s - a)*(s - b)*(s - c))
print("The area of triangle: " + str(area))

#ex23
import math
s = int(input("Enter the length of the side: "))
n = int(input("Enter the number of sides: "))
area = n*(s**2/(4*math.tan(math.pi/n)))
print("Area: " + str(area))

#ex24
d = int(input("Enter number of days: "))
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
s = int(input("Enter number of seconds: "))
t = d*86400 + h*3600 + m*60 + s
print("Total time in seconds: " + str(t))

#ex25
time = float(input("Enter time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

#ex26
import time
now = time.asctime(time.localtime(time.time()))
print("Local current time :", now)

#ex27
h = int(input("Your height in meters: "))
w = int(input("Your weight in kilograms: "))
bmi = w/(h**2)
print("Your BMI: " + str(bmi))

#ex28
t = int(input("Enter the temperature: "))
v = int(input("Enter the wind speed: "))
wci = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)
print("WCI: " + str(wci))

#ex29
tc = int(input("Enter temperature in celsius: "))
tf = (tc*(9/5)) + 32
tk = tc + 273.15
print("Your temperature in Fahrenheit: " + str(tf), "In Kelvin: " + str(tk))

#ex30
pascal = int(input("Enter pressure in kilopascals: "))
psq = pascal*0.145
mer = pascal*7.5
atm = 0.009
print("PSQ: " + str(psq), "Mercury: " + str(mer), "Atmosphere: " + str(atm))

#ex31
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return sum
n = int(input("Enter 4 digit number: "))
print(getSum(n))

#ex32
number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))
print("Sorted numbers: " + str(min(number1, number2, number3)), str(number1+number2+number3-min(number1, number2, number3)-max(number1, number2, number3)), str(max(number1, number2, number3)))

#ex33
n = int(input())
print("Just price: {:.2f}".format(n*3.49),"\ndiscount is 60%: {:.2f}".format(n*3.49*0.6), "\nthen total price: ","{:.2f}".format(n*0.4*3.49))
