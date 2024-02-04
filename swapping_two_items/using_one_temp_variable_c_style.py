def main():
    a = 1
    b = 2

    temp = a # a, b, temp = 1, 2, 1
    a = b    # a, b, temp = 2, 2, 1
    b = temp # a, b, temp = 2, 1, 1 

    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()