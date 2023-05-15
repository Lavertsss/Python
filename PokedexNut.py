import random
question = input("Hello Welcome to the Pokémon Number Generator. Do you wanna roll the dice? \n").lower()
randomizer = random.randint(0, 20)
###################################
if question == "yes":
    print(f"Your Pokedex entry was {randomizer}.")
elif question == "no":
    print("Useless bitch")
else:
    print("Useless bitch")
###################################
if question == "yes".lower():
    if randomizer == 0:
        print("??? ")
    if randomizer == 1:
        print("Bulbasaur. Fuck it. ")
    if randomizer == 2:
        print("Ivysaur. Fuck it.")
    if randomizer == 3:
        venesaur = random.randint(0, 1)
        if randomizer == 3 and venesaur == 0:
            print("Venesaur. Fuck it.")
        elif randomizer == 3 and venesaur == 1:
            print("Mega Venesaur. Fuck it.")
    if randomizer == 4:
        print("Charmander. Fuck it.")
    if randomizer == 5:
        print("Charmeleon. Fuck it.")
    if randomizer == 6:
        charizard = random.randint(0, 2)
        if randomizer == 6 and charizard == 0:
            print("Charizard. Double fuck it.")
        elif randomizer == 6 and charizard == 1:
            print("Mega Charizard X. Triple fuck it.")
        elif randomizer == 6 and charizard == 2:
            print(" Mega Charizard Y. Triple fuck it.")
    if randomizer == 7:
        print("Squirtle. Fuck it.")
    if randomizer == 8:
        print("Wartortle. Mid-fuck. Do it if you want.")
    if randomizer == 9:
        blastoise = random.randint(0, 1)
        if randomizer == 9 and blastoise == 0:
            print("Blastoise. Big fuck.")
        elif randomizer == 9 and blastoise == 1:
            print("Mega Blastoise. Utterly big fuck.")
    if randomizer == 10:
        print("Caterpie. Fuck made for women.")
    if randomizer == 11:
        print("Metapod. Low-tier fuck. Best to just not do it. Your choice though.")
    if randomizer == 12:
        print("Butterfree. Fuck it.")
    if randomizer == 13:
        print("Weedle. Fuck made for women.")
    if randomizer == 14:
        print("Kakuna. Honestly made to be a buttplug...")
    if randomizer == 15:
        beedrill = random.randint(0, 1)
        if randomizer == 15 and beedrill == 0:
            print("Beedrill. Fuck made for women.")
        elif randomizer == 15 and beedrill == 1:
            print("Mega Beedrill. Triple fuck made for women.")
    if randomizer == 16:
        print("Pidgey. Petite Fuck.")
    if randomizer == 17:
        print("Pidgeotto. Fuck it")
    if randomizer == 18:
        pidgeot = random.randint(0, 1)
        if randomizer == 18 and pidgeot == 0:
            print("Pidgeot. Fuck it.")
        elif randomizer == 18 and pidgeot == 1:
            print("Mega Pidgeot. Double fuck it.")
    if randomizer == 19:
        rattata = random.randint(0, 1)
        if randomizer == 19 and rattata == 0:
            print("Rattata. Petite fuck.")
        elif randomizer == 19 and rattata == 1:
            print("Alolan Rattata. Petite foreign fuck.")
    if randomizer == 20:
        raticate = random.randint(0, 1)
        if randomizer == 20 and raticate == 0:
            print("Raticate. Nyc type fuck.")
        elif randomizer == 20 and raticate == 1:
            print("Alolan Raticate. African foreign fuck. ")
else:
    print("Rot in hell.")
#########################################################
