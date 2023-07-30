# height = 1.8288
# weight = 58.96696
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
BMI = float(weight) / float(height) ** 2
BMI_INT = (int(BMI))
# "{:.2f}".format
if BMI_INT < 18.5:
    print(f"YOUR BMI IS {BMI_INT}.YOU ARE UNDERWEIGHT!")
elif BMI_INT < 25:
    print(f"YOUR BMI IS {BMI_INT}.YOU ARE NORMAL WEIGHT!")
elif BMI_INT < 30:
    print(f"YOUR BMI IS {BMI_INT}.YOU ARE OVERWEIGH!T")
elif BMI_INT < 35:
    print(f"YOUR BMI IS {BMI_INT}.YOU ARE OBESE!")
elif BMI_INT >= 35:
    print(f"YOUR BMI IS {BMI_INT}.YOU ARE CLINICALLY OBESE!")
else:
    print(f"YOUR BMI IS {BMI_INT}.Unidentifiable")
