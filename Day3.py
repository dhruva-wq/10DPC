#Day 3 practice

Score = int(input("Enter your mark: "))

if Score > 100 or Score < 0:
    print("Invalid marks! Enter between 0 and 100")
elif Score >= 90:
    print("You got an A grade")
elif Score >= 80:
    print("You got a B grade")
elif Score >= 70:
    print("You got a C grade")
else:
    print("Fail")

#Nested condition
#Assignment

age = int(input("Enter your age: "))

pro = input("Enter your sub plan: ")

if age >= 18:
    if pro :
        print("Full Access")
    else:
        print("Learn Mode")
else:
    print("Junior level - not allowed for this site")

#Ternary condition

status = "Adult" if age >= 18 else "Minor"
print(status)