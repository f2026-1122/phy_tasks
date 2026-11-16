# 𝗡𝗔𝗠𝗘: 𝗔𝗟𝗜 𝗜𝗠𝗥𝗔𝗡

# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟭: 𝗣𝗿𝗲𝗱𝗶𝗰𝘁 𝘁𝗵𝗲 𝗢𝘂𝘁𝗽𝘂𝘁

print("Exercise 1 - Question 1:", 7 / 2)
print("Exercise 1 - Question 2:", 7 // 2)
print("Exercise 1 - Question 3:", "7" + "2")
print("Exercise 1 - Question 4:", 7 % 2)
print("Exercise 1 - Question 5:", 2 + 3 * 4 ** 2)
print("Exercise 1 - Question 6:", bool("0"))

# SOLUTION / TRACED OUTPUT:
# Exercise 1 - Question 1: 3.5
# Exercise 1 - Question 2: 3
# Exercise 1 - Question 3: 72
# Exercise 1 - Question 4: 1
# Exercise 1 - Question 5: 50
# Exercise 1 - Question 6: True


# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟮: 𝗙𝗶𝗻𝗱 𝗮𝗻𝗱 𝗙𝗶𝘅 𝘁𝗵𝗲 𝗕𝘂𝗴𝘀

person_name = input("Name: ")
print("Hello", person_name)

age = int(input("Age: "))
print("Next year:", age + 1)

print("Done")

# SOLUTION / SAMPLE OUTPUT:
# Name: Ali
# Hello Ali
# Age: 18
# Next year: 19
# Done
# Note: input() gives text, so int() converts the age to a number.
# Python is case-sensitive, so use the same variable-name spelling.


# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟯: 𝗕𝗶𝗹𝗹 𝗦𝗽𝗹𝗶𝘁𝘁𝗲𝗿

total_bill = int(input("Total bill (whole rupees): "))
number_of_friends = int(input("Number of friends: "))

each_pays = total_bill // number_of_friends
left_over = total_bill % number_of_friends
exact_share = total_bill / number_of_friends

print("Each pays:", each_pays)
print("Left over:", left_over)
print("Exact share:", exact_share)
print("Floor division share:", each_pays)

# SOLUTION / SAMPLE OUTPUT:
# Total bill (whole rupees): 1000
# Number of friends: 3
# Each pays: 333
# Left over: 1
# Exact share: 333.3333333333333
# Floor division share: 333


# 𝗧𝗔𝗦𝗞 𝟭: 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀 𝗮𝗻𝗱 𝗗𝗮𝘁𝗮 𝗧𝘆𝗽𝗲𝘀

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
student_answer = input("Are you a student? (yes/no): ").strip().lower()
is_student = student_answer == "yes"

print(student_name, type(student_name))
print(student_age, type(student_age))
print(height, type(height))
print(is_student, type(is_student))

# SOLUTION / SAMPLE OUTPUT:
# Enter your name: Ali Imran
# Enter your age: 18
# Enter your height in metres: 1.7
# Are you a student? (yes/no): yes
# Ali Imran <class 'str'>
# 18 <class 'int'>
# 1.7 <class 'float'>
# True <class 'bool'>


# 𝗧𝗔𝗦𝗞 𝟮: 𝗧𝗲𝗺𝗽𝗲𝗿𝗮𝘁𝘂𝗿𝗲 𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)

# SOLUTION / SAMPLE OUTPUT:
# Enter temperature in Celsius: 25
# Fahrenheit: 77.0
# Kelvin: 298.15


# 𝗧𝗔𝗦𝗞 𝟯: 𝗦𝗶𝗺𝗽𝗹𝗲 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number != 0:
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Modulus:", first_number % second_number)
else:
    print("Division: Not possible (cannot divide by zero)")
    print("Floor division: Not possible (cannot divide by zero)")
    print("Modulus: Not possible (cannot divide by zero)")

print("Power:", first_number ** second_number)

# SOLUTION / SAMPLE OUTPUT:
# Enter first number: 10
# Enter second number: 3
# Addition: 13.0
# Subtraction: 7.0
# Multiplication: 30.0
# Division: 3.3333333333333335
# Floor division: 3.0
# Modulus: 1.0
# Power: 1000.0


# 𝗧𝗔𝗦𝗞 𝟰: 𝗦𝗮𝘃𝗶𝗻𝗴𝘀 𝗧𝗿𝗮𝗰𝗸𝗲𝗿

savings = 1000
print("Starting savings:", savings)

savings += 500
print("After gift:", savings)

savings -= 300
print("After buying books:", savings)

savings *= 2
print("After doubling:", savings)

# SOLUTION / OUTPUT:
# Starting savings: 1000
# After gift: 1500
# After buying books: 1200
# After doubling: 2400


# 𝗧𝗔𝗦𝗞 𝟱: 𝗦𝗰𝗵𝗼𝗹𝗮𝗿𝘀𝗵𝗶𝗽 𝗖𝗵𝗲𝗰𝗸

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_check = marks >= 80
attendance_check = attendance >= 75
qualifies = marks_check and attendance_check

print("Marks 80 or more:", marks_check)
print("Attendance 75% or more:", attendance_check)
print("Qualifies for scholarship:", qualifies)

# SOLUTION / SAMPLE OUTPUT:
# Enter your marks: 85
# Enter your attendance percentage: 80
# Marks 80 or more: True
# Attendance 75% or more: True
# Qualifies for scholarship: True
