# 1st input:
height = input("Please input your height in meters (e.g: 1.70)\n")
# 2nd input:
weight = input("Please input your weight in kilograms (e.g: 72)\n")

# calculation
bmi = float(weight) / (float(height) ** 2)
bmi_as_int = int(bmi)
print("Your BMI is: " + str(bmi_as_int) + " and classifies as normal weight\n")