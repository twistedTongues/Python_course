print("\n\t\t\tUnits:metric")

name = str(input("Enter your name: "))
height = float(input("Input your height in meters(For instance:1.89): "))
weight = float(input("Input your weight in kilogram(For instance:69): "))
age = int(input("Input your age: "))
sex = str(input("Input your sex: "))
user_info = {name: [height, weight, age, sex]}

bmi = (weight/(height*height))

print("Your body mass index (or BMI) is: ", round(bmi, 2))

if sex == 'male':
    if bmi < 15:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Very severely underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
    elif 15 < bmi < 16:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Severely underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
    elif 16 < bmi < 18.5:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
    elif 18.5 < bmi < 25:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Normal(healthy weight):\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif 25 < bmi < 30:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Overweight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif 30 < bmi < 35:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Moderately obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif 35 < bmi < 40:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Severely obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif bmi > 40:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Very severely obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    else:
        print("There is an error with your input")
else:
    if bmi < 18.5:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
    elif 18.5 < bmi < 24.9:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Healthy weight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif 25 < bmi < 29.9:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Overweight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    elif bmi > 30:
        print("\n\t\t\tYour BMI is", round(bmi, 2), "Moderately obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
    else:
        print("There is an error with your input")
print('\n\n10' + '=' * (int(round(bmi, 0))-10-1)+'|'+'=\
'*(60-int(round(bmi, 0))-1)+'60')
#
print(user_info.get(str(input("Enter your login: "))))
while True:
    exit = str(input("Type 'exit()'"))
    if exit == 'exit()':
        break
    else:
        print("\n\t\t\tUnits:metric")

        name = str(input("Enter your name: "))
        height = float(input("Input your height in meters(For instance:1.89): \
"))
        weight = float(input("Input your weight in kilogram(For instance:69): \
"))
        age = int(input("Input your age: "))
        sex = str(input("Input your sex: "))
        user_info = {name: [height, weight, age, sex]}

        bmi = (weight/(height*height))

        print("Your body mass index (or BMI) is: ", round(bmi, 2))

        if sex == 'male':
            if bmi < 15:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Very severely underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
            elif 15 < bmi < 16:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Severely underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
            elif 16 < bmi < 18.5:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
            elif 18.5 < bmi < 25:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Normal(healthy weight):\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif 25 < bmi < 30:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Overweight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif 30 < bmi < 35:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Moderately obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif 35 < bmi < 40:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Severely obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif bmi > 40:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Very severely obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            else:
                print("There is an error with your input")
        else:
            if bmi < 18.5:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Underweight:\
\nIt is important to know whether a serious disease \
or other conditions have caused the emaciation. Whatever \
the case, medical help is advisable.\n\t\t\tPossible causes:  \
\nUndernourishment \
\nMaldigestion \
\nEating disorders: anorexia, bulimia \
\nSlimming caused by a disease")
            elif 18.5 < bmi < 24.9:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Healthy weight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif 25 < bmi < 29.9:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Overweight:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            elif bmi > 30:
                print("\n\t\t\tYour BMI is", round(bmi, 2), "Moderately obese:\
\nPlay physical games and do physical \
exercise at least for an hour daily at \
moderate to vigorous intensity.Try out a \
variety of foods, including fresh \
fruit and vegetables.Eat and drink what \
you like, but not too much sweets \
and sweetened drinks.")
            else:
                print("There is an error with your input")
    print('\n\n10' + '=' * (int(round(bmi, 0))-10-1)+'|'+'=\
'*(60-int(round(bmi, 0))-1)+'60')
