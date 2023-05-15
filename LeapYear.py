
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is a leap year")
elif year % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
