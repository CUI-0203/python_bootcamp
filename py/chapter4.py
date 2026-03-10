#CONDITIONAL STATEMENTS


age = 18

if age >= 18:
    print("YOU are an adult.")
else:
    print("You are a minor.")


score = 85

if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")


user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")


    day = "Saturday"
    if day == "Saturday" or day == "Sunday":
        print("It's the weekend!")
    else:
        print("It's a weekday.")
        

#Nested conditions
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("It's a great day for outdoor activities!")
    else:
        print("It's sunny but a bit chilly.")

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi}.")
if bmi < 18.5:
    print("You are underweight.")

elif bmi < 24.9:
    print("You have a normal weight.")

elif bmi < 29.9:
    print("You are overweight.")

else:
    print("You are obese.")


