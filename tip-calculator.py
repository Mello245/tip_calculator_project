# A program which can be used to calculate how much each party should pay on a bill (and calculate the designated tip amount)
#Program needs to; 
# Take input from the user - bill amount X
# Store the input as a variable - "bill_amount" X
# Take input from the user - amount of people to split between 
# Store the input as a variable - "no_of_people" 
# Take input from the user - tip percentage 
# Store the input as a variable - "tip_percentage"
# Create a new variable using the selected tip percentage and the total bill = "bill_plus_tip_amount"
# Calculate how much each person owes of the new bill+tip variable 



#Step One 
bill_amount = input("What is the bill amount?")
bill_amount = float(bill_amount)
print(bill_amount)

#Step Two 
no_of_people = input("How many people to split between?")
no_of_people = float(no_of_people)
print(no_of_people)

#Step Three 
tip_percentage = input("How much would you like to tip (%) 5, 10, 20 or 30 ?")
tip_percentage = float(tip_percentage)
print(tip_percentage)

#Step Four 
bill_plus_tip_amount = (float(bill_amount+(bill_amount*tip_percentage/100)))
print(bill_plus_tip_amount)

#Step Five 
amount_each_person_owes = (bill_plus_tip_amount/no_of_people)
amount_each_person_owes = round(amount_each_person_owes,2)
amount_each_person_owes = (str(amount_each_person_owes))

print("Each person owes" + " £" + amount_each_person_owes)