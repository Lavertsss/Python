row1 = ["1 1", "2 1", "3 1"]
row2 = ["1 2", "2 2", "3 2"]
row3 = ["1 3", "2 3", "3 3"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")
