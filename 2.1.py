w1 = int(input("Enter the vertical position of white rook: "))
w2 = int(input("Enter the horizontal position of white rook: "))
b1 = int(input("Enter the vertical position of black rook: "))
b2 = int(input("Enter the horizontal position of black rook: "))
if (w1 - b1)*(w2 - b2) == 0:
    print("YES")
else:
    print("NO")