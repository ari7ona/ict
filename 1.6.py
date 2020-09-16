charge = float(input("Enter you charge of the food: "))
tip = 0.18 * charge
tax = 0.10 * charge
total = charge + tip + tax
print("Charge: $" + "{0:.2f}".format(float(charge)), "Tip: $" + "{0:.2f}".format(float(tip)), "Tax: $" + "{0:.2f}".format(float(tax)), "Total: $" + "{0:.2f}".format(float(total)))
