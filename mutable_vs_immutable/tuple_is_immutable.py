def main():
    # tuple is immutable
    a = (0, 1, 2)
    try:
        a[1] = "1"
        print(f"{a = }")
    except TypeError as e:
        print(e)

    # tuple is immutable, but items in tuple can be mutable
    a = (1, [1, 2, 3], 'Hello')
    a[1][0] = 'one'
    print(f"{a = }")

if __name__ == "__main__":
    main()

