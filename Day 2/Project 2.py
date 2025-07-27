print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


share = round((bill + tip*bill*0.01)/people,3)
print(f"The Each Person Should Pay ${share}")
