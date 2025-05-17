#given that  𝐵𝑀𝐼 = weight divided by the square of height
#store the weight in kg and height in m to two variables
weight = 82
height = 1.85
#calculate and print 
BMI = weight/height**2
print("your BMI is " + str(BMI), end=". ")

#based on information given classsify BMI
if BMI < 18.5:
    print("you are underweight")
elif BMI > 30:
    print("you are obese")
else:
    print("you have a normal BMI")