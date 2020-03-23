def enlarge(i):
    return i * 100


# "if this script is run from the command-line, then ..."
if __name__ == "__main__":
    my_number = float(input("Input a number"))

    n = enlarge(my_number)
    print(n)

