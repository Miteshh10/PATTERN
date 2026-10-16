
n = 6

for i in range(1, n + 1):

    # Print spaces
    for j in range(i - 1):
        print(" ", end="")

    # Print stars
    for j in range(n - i + 1):
        print("*", end="")

    # Move to the next row
    print()
