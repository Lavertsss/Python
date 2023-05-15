import random
names_string = input("Give me a list of names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " will pay for dinner.")
print("----------------------------------------------------------")
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " will pay for dinner.")
# Joseph, Elvedin, Joshua, Chris, Donovan, Paul, Jack, Leroy
