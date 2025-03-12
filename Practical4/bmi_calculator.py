#given that  𝐵𝑀𝐼 = weight divided by the square of height
weight = 87
height = 1.87
BMI = weight/height**2
print("your BMI is " + str(BMI), end=". ")

if BMI < 18.5:
    print("you are underweight")
elif BMI > 30:
    print("you are obese")
else:
    print("you have a normal BMI")