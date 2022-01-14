from typing import Collection


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

raw = int(position[0])
col = int(position[1])


map[col-1][raw-1] = "X"

print(f"{row1}\n{row2}\n{row3}")