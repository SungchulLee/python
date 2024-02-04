def main():
    a = 3
    a //= 2 # // is supported by __ifloordiv__
    print(a)

    a = 3
    a = a // 2 # // is supported by __floordiv__
    print(a)

if __name__ == "__main__":
    main()