def main():
    a = 3
    a -= 2 # - is supported by __isub__
    print(a)

    a = 3
    a = a - 2 # - is supported by __sub__
    print(a)

if __name__ == "__main__":
    main()