print("\n\t\t\tUnits:metric")
height = float(input("Input your height in meters(For instance:1.89): "))
weight = float(input("Input your weight in kilogram(For instance:69): "))

bmi = (weight/(height*height))
print("Your body mass index (or BMI) is: ", round(bmi, 2))
if bmi < 15:
    print("Your BMI is", round(bmi, 2), "Very severely underweight")
elif 15 < bmi < 16:
    print("Your BMI is", round(bmi, 2), "Severely underweight")
elif 16 < bmi < 18.5:
    print("Your BMI is", round(bmi, 2), "Underweight")
elif 18.5 < bmi < 25:
    print("Your BMI is", round(bmi, 2), "Normal (healthy weight)")
elif 25 < bmi < 30:
    print("Your BMI is", round(bmi, 2), "Overweight")
elif 30 < bmi < 35:
    print("Your BMI is", round(bmi, 2), "Moderately obese")
elif 35 < bmi < 40:
    print("Your BMI is", round(bmi, 2), "Severely obese")
elif bmi > 40:
    print("Your BMI is", round(bmi, 2), "Very severely obese")
else:
    print("There is an error with your input")

print('20' + '=' * (int(round(bmi, 0))-20-1)+'|'+'=\
'*(50-int(round(bmi, 0))-1)+'50')
