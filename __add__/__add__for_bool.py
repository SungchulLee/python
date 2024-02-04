def main():
    a = True
    b = True
    c1 = a + b
    c2 = bool.__add__(a, b)
    c3 = a.__add__(b)
    print(c1)
    print(c2)
    print(c3)

if __name__ == "__main__":
    main()