# Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_bill_with_tip = bill + (bill * tip_percent)
amount_per_person = total_bill_with_tip / people
final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount}")
