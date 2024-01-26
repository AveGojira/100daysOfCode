print("Welcome to the Tip Calculator!\n")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? e.g. 10, 12, or 15? ")
persons_paying = input("How many people to split the bill? ")
percentage_tip = (int(tip) / 100) + 1
split_bill = "{:.2f}".format(float(bill) * float(percentage_tip) / int(persons_paying))
print(f"Each person should pay: ${split_bill}")