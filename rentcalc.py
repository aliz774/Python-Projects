# Total Inputs from users:

# Total rent.
# Total expense on food. 
# Electricity bill.
# Total number of persons living in Room/flat.
# Maintainance or other expense.

# Output:
# Total amount you have to pay.


rent = int(input("Enter your room/flat rent : "))
food = int(input("Enter the total expense on food this month : "))
electricity_bill = int(input("Enter the total of electricity bill: "))
other_expense = int(input("Enter the total amount of other expense : "))
persons = int(input("Enter the number of persons living in Room/Flat : "))

output = (rent + food + electricity_bill + other_expense)// persons

print("Each person will have to pay : ", output)