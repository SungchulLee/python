def main():
    a = 1.j
    b = 1.j
    c1 = a + b
    c2 = complex.__add__(a, b)
    c3 = a.__add__(b)
    print(c1)
    print(c2)
    print(c3)

if __name__ == "__main__":
    main()