print("Welcome to my tip calculator from day 2 of learning python!")
total_bill = float(input("What was the total bill?"))
tip_percentage = float(input("What percentage of tip would you like to give?"))
people_splitting = int(input("How many people are splitting the bill?"))
each_person_bill = (total_bill * (1 + tip_percentage/100)) / people_splitting
print(f"Each Person should pay: ${each_person_bill:.2f}")
