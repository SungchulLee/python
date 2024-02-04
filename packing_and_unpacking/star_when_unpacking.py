def main():
    a, b, *_, c, _ = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

    a, _, b, *_, c = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

    _, a, b, c, *_ = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

    a, _, _, b, *_, c = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

    *_, a, b, _, c = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

    _, a, *_, b, c = (1, 2, 3, 4, 5, 6)
    print(a, b, c)

if __name__ == "__main__":
    main()