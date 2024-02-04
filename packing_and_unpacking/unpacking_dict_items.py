def main():
    a, b, c = {'one' : 1, 'two' : 2, 'three' : 3}.items()
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

    (a0, a1), (b0, b1), (c0, c1) = {'one' : 1, 'two' : 2, 'three' : 3}.items()
    print(a0, a1)
    print(b0, b1)
    print(c0, c1)

if __name__ == "__main__":
    main()