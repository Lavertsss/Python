import collections


def answer():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    question = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while question == "encode":
        message = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))
        encoded = question + message + shift_number
        print(f"Here's the encoded result: {encoded}")
        yn = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        print(yn)
        if yn == "yes":
            answer()
        elif yn == "no":
            exit()
        else:
            print("Answer typed incorrectly. ")
            exit()
    while question == "decode":
        message = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))
        encoded = question + message + shift_number
        print(f"Here's the decoded result: {encoded}")
        yn = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        print(yn)
        if yn == "yes":
            answer()
        elif yn == "no":
            exit()
        else:
            print("Answer typed incorrectly. ")
            exit()

answer()
