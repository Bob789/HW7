num: int = int(input("Enter number :"))
center_position: int = int((num / 2) + 1)
space: int = center_position
for x in range(1, num + 1, 2):
    print()
    space -= 1
    print(" " * space, end="")
    for y in range(1, x + 1):
        print(f"{y}", end="")
for x in range(num - 2, 0, -2):
    print()
    space += 1
    print(" " * space, end="")
    for y in range(1, x + 1):
        print(f"{y}", end="")
