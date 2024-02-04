def main():
    a = 1
    b = 2

    a, b = b, a # packing and unpacking

    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()