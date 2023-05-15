print("Welcome to Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
score = name1 + name2
score2 = score.count("a")

if score2 < 10 or score2 > 90:
    print(f"Your score is {score2}, You go together like coke and mentos")
elif (score2 >= 40) and (score2 <= 50):
    print(f"Your score is {score2}, you are alright together")
else:
    print(f"Your score is {score2}")
