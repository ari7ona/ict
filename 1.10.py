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
