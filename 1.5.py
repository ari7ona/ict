s_c = int(input("Enter the number of small containers: "))
l_c = int(input("Enter the number of large containers: "))
refund = (s_c * 0.10) + (l_c * 0.25)
print("Your refund is $" + "{0:.2f}".format(float(refund)))