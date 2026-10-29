
# 1. Take an integer from the user and check whether it is even or odd.
print("--- Task 1: Even or Odd ---")
num1 = int(input("Ek integer number enter karein: "))
if num1 % 2 == 0:
    print("  Even .")
else:
    print("  Odd .")
print()

# 2. Take a  and check whether it is positive or negative.
print("--- Task 2: Positive or Negative ---")
num2 = float(input("Ek  number enter karein: "))
if num2 >= 0:
    print("  Positive .")
else:
    print("  Negative .")
print()

# 3. Take a person's age and check whether they are eligible to vote. Assume the minimum voting age is 18.
print("--- Task 3: Voting Eligibility ---")
age_vote = int(input("Apni age enter karein: "))
if age_vote >= 18:
    print("  eligible .")
else:
    print("  not eligible  .")
print()

# 4. Take two numbers from the user and print the greater number. If both numbers are equal, display an appropriate message.
print("--- Task 4: Greater Number Check ---")
n1 = float(input("Pehla number enter karein: "))
n2 = float(input("Dusra number enter karein: "))
if n1 > n2:
    print("  Pehla number bara hai:", n1)
elif n2 > n1:
    print("  Dusra number bara hai:", n2)
else:
    print("  Dono numbers barabar hain.")
print()

# 5. Take a password from the user and check whether it matches a predefined password.
print("--- Task 5: Password Check ---")
correct_password = "password123"
user_pass = input("Password enter karein: ")
if user_pass == correct_password:
    print("Password match ho gaya.")
else:
    print("Ghalat password!")
print()

# 6. Take a student's marks and check whether the student has passed or failed. Assume 50 marks are required to pass.
print("--- Task 6: Pass or Fail Check ---")
marks = float(input("Apne marks enter karein: "))
if marks >= 50:
    print(" pass !")
else:
    print(" fail .")
print()

# 7. Take a student's marks out of 100 and assign a grade according to the criteria.
print("--- Task 7: Grading System ---")
grade_marks = float(input("Marks out of 100 enter karein: "))
if grade_marks >= 90 and grade_marks <= 100:
    print("Grade: A+")
elif grade_marks >= 80 and grade_marks < 90:
    print("Grade: A")
elif grade_marks >= 70 and grade_marks < 80:
    print("Grade: B")
elif grade_marks >= 60 and grade_marks < 70:
    print("Grade: C")
elif grade_marks >= 50 and grade_marks < 60:
    print("Grade: D")
elif grade_marks >= 0 and grade_marks < 50:
    print("Grade: Fail")
else:
    print("Ghalat marks enter kiye gaye hain!")
print()

# 8. Take a number from the user and determine whether it is positive, negative, or zero.
print("--- Task 8: Positive, Negative or Zero ---")
num_check = float(input("Ek number enter karein: "))
if num_check > 0:
    print(" Positive .")
elif num_check < 0:
    print(" Negative .")
else:
    print(" Zero .")
print()

# 9. Create a simple calculator that takes two numbers and an operator (+, -, *, /).
print("--- Task 9: Simple Calculator ---")
calc_n1 = float(input("Pehla number enter karein: "))
calc_n2 = float(input("Dusra number enter karein: "))
operator = input("Operator enter karein (+, -, *, /): ")

if operator == '+':
    print("Result:", calc_n1 + calc_n2)
elif operator == '-':
    print("Result:", calc_n1 - calc_n2)
elif operator == '*':
    print("Result:", calc_n1 * calc_n2)
elif operator == '/':
    if calc_n2 != 0:
        print("Result:", calc_n1 / calc_n2)
    else:
        print("Error: Zero se division nahi ho sakti!")
else:
    print("Ghalat operator enter kiya gaya hai!")
print()

# 10. Take the temperature in input and display messages.
print("--- Task 10: Temperature Message ---")
temp = float(input("Temperature enter karein: "))
if temp > 35:
    print("Very Hot")
elif temp >= 25 and temp <= 35:
    print("Hot")
elif temp >= 15 and temp <= 24:
    print("Moderate")
elif temp >= 5 and temp <= 14:
    print("Cold")
else:
    print("Very Cold")
print()

# 11. Create a simple ticket-pricing program based on age.
print("--- Task 11: Ticket Pricing ---")
ticket_age = int(input("Age enter karein ticket ke liye: "))
if ticket_age < 5:
    print("Free")
elif ticket_age >= 5 and ticket_age <= 12:
    print("Child Ticket")
elif ticket_age >= 13 and ticket_age <= 17:
    print("Teen Ticket")
elif ticket_age >= 18 and ticket_age <= 59:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")
print()

# 12. Create an electricity bill calculator using units.
print("--- Task 12: Electricity Bill Calculator ---")
units = float(input("Consumed units enter karein: "))
if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = (100 * 10) + ((units - 100) * 15)
else:
    bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)
print("Total Electricity Bill: Rs.", bill)
print()

# 13. Take a user's age and monthly income for loan eligibility.
print("--- Task 13: Loan Eligibility (Simple) ---")
loan_age = int(input("Age enter karein: "))
loan_income = float(input("Monthly income enter karein (Rs.): "))
if loan_age >= 21 and loan_income >= 50000:
    print("Aap loan ke liye eligible hain!")
else:
    print("Aap loan ke liye eligible nahi hain.")
print()

# 14. Take the total shopping amount and calculate the discount category.
print("--- Task 14: Shopping Discount ---")
shopping_amt = float(input("Total shopping amount enter karein (Rs.): "))
if shopping_amt < 2000:
    print("No Discount")
elif shopping_amt >= 2000 and shopping_amt <= 4999:
    print("5% Discount")
elif shopping_amt >= 5000 and shopping_amt <= 9999:
    print("10% Discount")
else:
    print("20% Discount")
print()

# 15. Take the number of GB used by a customer and display usage category.
print("--- Task 15: GB Usage Category ---")
gb_used = float(input("Used GBs enter karein: "))
if gb_used < 5:
    print("Low Usage")
elif gb_used >= 5 and gb_used <= 20:
    print("Normal Usage")
elif gb_used >= 21 and gb_used <= 50:
    print("High Usage")
else:
    print("Very High Usage")
print()

# 16. Take an employee's years of experience and monthly salary for bonus.
print("--- Task 16: Employee Bonus ---")
exp = float(input("Years of experience enter karein: "))
emp_salary = float(input("Monthly salary enter karein (Rs.): "))

if exp < 1:
    print("No Bonus")
elif exp >= 1 and exp <= 3:
    print("5% Bonus")
elif exp > 3 and emp_salary < 100000:
    print("10% Bonus")
else:
    print("15% Bonus")
print()

# 17. Take an integer and determine its sign and parity.
print("--- Task 17: Sign and Parity ---")
int_num = int(input("Ek integer enter karein: "))
if int_num == 0:
    print("Zero")
elif int_num > 0:
    if int_num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    if int_num % 2 == 0:
        print("Negative and even")
    else:
        print("Negative and odd")
print()

# 18. Ask the user to enter a username and password with nested checks.
print("--- Task 18: Nested Login System ---")
saved_user = "admin"
saved_pass = "secret123"

input_user = input("Username enter karein: ")
if input_user == saved_user:
    input_pass = input("Password enter karein: ")
    if input_pass == saved_pass:
        print("Login Successful!")
    else:
        print("Ghalat password! Unsuccessful login.")
else:
    print("Ghalat username! Unsuccessful login.")
print()

# 19. Take the account balance and withdrawal amount as input with validation.
print("--- Task 19: ATM Withdrawal ---")
balance = float(input("Account balance enter karein (Rs.): "))
withdrawal = float(input("Withdrawal amount enter karein (Rs.): "))

if withdrawal > 0:
    if balance >= withdrawal:
        balance -= withdrawal
        print("Withdrawal successful! Remaining balance: Rs.", balance)
    else:
        print("Insufficient balance! Account mein kafi raqam nahi hai.")
else:
    print("Ghalat withdrawal amount! Amount zero se bari honi chahiye.")
print()

# 20. Take the user's age and monthly income as input with sequential nested checks.
print("--- Task 20: Sequential Loan Eligibility ---")
u_age = int(input("Age enter karein: "))
if u_age >= 21:
    u_income = float(input("Monthly income enter karein (Rs.): "))
    if u_income >= 50000:
        print("Aapne basic loan eligibility criteria poora kar liya hai!")
    else:
        print("Age poori hai lekin monthly income Rs. 50,000 se kam hai.")
else:
    print("Aapki age 21 saal se kam hai, is liye aap eligible nahi hain.")