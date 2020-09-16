d = int(input("Enter number of days: "))
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
s = int(input("Enter number of seconds: "))
t = d*86400 + h*3600 + m*60 + s
print("Total time in seconds: " + str(t))
