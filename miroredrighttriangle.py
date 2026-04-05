row = int(input("Enter the number of rows: "))

# Top half
for i in range(1, row + 1):
    for j in range(i):
        print("* ", end="")
    print()

# Bottom half (include the middle again)
for i in range(row, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()