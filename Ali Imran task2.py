# 𝗡𝗔𝗠𝗘: 𝗔𝗟𝗜 𝗜𝗠𝗥𝗔𝗡

# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟭: 𝗣𝗿𝗲𝗱𝗶𝗰𝘁 𝘁𝗵𝗲 𝗢𝘂𝘁𝗽𝘂𝘁

print("Python"[1:4])
print("banana".count("an"))
print("Hello"[-1])
print("Zebra" < "apple")
print(5 > 3 and 2 > 4)
print(not "")

# SOLUTION / TRACED OUTPUT:
# yth
# 2
# o
# True
# False
# True


# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟮: 𝗙𝗶𝗻𝗱 𝗮𝗻𝗱 𝗙𝗶𝘅 𝟰 𝗕𝘂𝗴𝘀

marks = int(input("Marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")

answer = input("Again? ")
if answer == "yes":
    print("Restarting...")

# SOLUTION / SAMPLE OUTPUT:
# Marks: 65
# Pass
# Again? yes
# Restarting...
# Note: if/else must be correctly indented. input() returns text,
# so int() converts marks to a number. The comparison uses ==.


# 𝗘𝗫𝗘𝗥𝗖𝗜𝗦𝗘 𝟯: 𝗦𝘁𝘂𝗱𝗲𝗻𝘁 𝗚𝗿𝗮𝗱𝗲𝗿

student_name = input("Student name: ").strip().title()
marks_text = input("Marks (0-100): ").strip()

if marks_text.isdigit():
    marks = int(marks_text)

    if marks > 100:
        print("Marks must be 0-100")
    elif marks >= 90:
        grade = "A"
        print(f"{student_name} scored {marks}/100 -> Grade {grade}")
    elif marks >= 80:
        grade = "B"
        print(f"{student_name} scored {marks}/100 -> Grade {grade}")
    elif marks >= 70:
        grade = "C"
        print(f"{student_name} scored {marks}/100 -> Grade {grade}")
    elif marks >= 50:
        grade = "D"
        print(f"{student_name} scored {marks}/100 -> Grade {grade}")
    else:
        grade = "F"
        print(f"{student_name} scored {marks}/100 -> Grade {grade}")
else:
    print("Please enter marks as a whole number.")

# SOLUTION / SAMPLE OUTPUT:
# Student name: ali imran
# Marks (0-100): 86
# Ali Imran scored 86/100 -> Grade B


# 𝗧𝗔𝗦𝗞 𝟭: 𝗡𝗮𝗺𝗲 𝗙𝗼𝗿𝗺𝗮𝘁𝘁𝗲𝗿 (𝗦𝘁𝗿𝗶𝗻𝗴 𝗠𝗲𝘁𝗵𝗼𝗱𝘀)

full_name = input("Enter your full name: ")
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())
print("Total characters:", len(full_name))
print("Number of 'a':", full_name.count("a"))

# SOLUTION / SAMPLE OUTPUT:
# Enter your full name: ayesha khan
# Uppercase: AYESHA KHAN
# Lowercase: ayesha khan
# Title case: Ayesha Khan
# Total characters: 11
# Number of 'a': 3


# 𝗧𝗔𝗦𝗞 𝟮: 𝗘𝗺𝗮𝗶𝗹 𝗕𝗿𝗲𝗮𝗸𝗱𝗼𝘄𝗻 (𝗜𝗻𝗱𝗲𝘅𝗶𝗻𝗴 𝗮𝗻𝗱 𝗦𝗹𝗶𝗰𝗶𝗻𝗴)

email = input("Enter your email: ")
at_position = email.find("@")

print("First character:", email[0])
print("Last character:", email[-1])
print("Position of @:", at_position)
print("Username:", email[:at_position])
print("Domain:", email[at_position + 1:])
print("Gmail address:", email.endswith("gmail.com"))

# SOLUTION / SAMPLE OUTPUT:
# Enter your email: ali.khan@gmail.com
# First character: a
# Last character: m
# Position of @: 8
# Username: ali.khan
# Domain: gmail.com
# Gmail address: True


# 𝗧𝗔𝗦𝗞 𝟯: 𝗥𝗲𝗽𝗼𝗿𝘁 𝗖𝗮𝗿𝗱 (𝗳-𝘀𝘁𝗿𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗧𝘆𝗽𝗲𝗰𝗮𝘀𝘁𝗶𝗻𝗴)

student_name = input("Enter your name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("----- Report Card -----")
print(f"Name: {student_name}")
print(f"Total: {total} out of 300")
print(f"Percentage: {percentage:.2f}%")

# SOLUTION / SAMPLE OUTPUT:
# Enter your name: Sara
# Enter marks for Subject 1: 78
# Enter marks for Subject 2: 85.5
# Enter marks for Subject 3: 90
# ----- Report Card -----
# Name: Sara
# Total: 253.5 out of 300
# Percentage: 84.50%


# 𝗧𝗔𝗦𝗞 𝟰: 𝗚𝗿𝗮𝗱𝗲 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿 (𝗶𝗳, 𝗲𝗹𝗶𝗳 𝗮𝗻𝗱 𝗲𝗹𝘀𝗲)

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 85:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 55:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# SOLUTION / SAMPLE OUTPUT:
# Enter your marks: 72
# Grade: B


# 𝗧𝗔𝗦𝗞 𝟱: 𝗟𝗼𝗴𝗶𝗻 𝗖𝗵𝗲𝗰𝗸𝗲𝗿 (𝗡𝗲𝘀𝘁𝗲𝗱 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀)

username = input("Enter username: ").strip().lower()
password = input("Enter password: ")

if username == "codestart":
    if password == "python123":
        print("Login successful. Welcome to CodeStart!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found.")

# SOLUTION / SAMPLE OUTPUT:
# Enter username:   CodeStart
# Enter password: python123
# Login successful. Welcome to CodeStart!
