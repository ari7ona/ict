number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))
print("Sorted numbers: " + str(min(number1, number2, number3)), str(number1+number2+number3-min(number1, number2, number3)-max(number1, number2, number3)), str(max(number1, number2, number3)))