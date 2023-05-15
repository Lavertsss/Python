import random
heads = 0
tails = 1
random_int = random.randint(0, 1)
answer = (input(f"Type {heads} for heads or {tails} for tails =  "))
if random_int == int(answer):
    print("Correct")
elif random_int != int(answer):
    print("Incorrect")
