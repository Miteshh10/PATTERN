for i in range(1, 7):

    # print spaces
    for j in range(5 - i):
        print(" ", end="")

    # print stars
    for j in range(i):
        print("*", end="")

    # move to next line
    print()