def answer():
    while question == "encode":
        print(message)
        print(shift_number)
        print(f"Here's the encoded result: {encoded}")
        print(yn)
        if yn == "yes":
            answer()
        elif yn == "no":
            exit()
        else:
            exit()
    if question == "decode":
        print(message)
        print(shift_number)
        print(f"Here's the decoded result: {encoded}")
        print(yn)
        if yn == "yes":
            answer()
        elif yn == "no":
            exit()
        else:
            exit()
print(type(answer())