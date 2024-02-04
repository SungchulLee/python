def main():
    a, b, _ = (1, 2, 3)
    print(a, b)
    print(a, b, _)

    a, _, b = (1, 2, 3)
    print(a, b)
    print(a, b, _)

    _, a, b = (1, 2, 3)
    print(a, b)
    print(a, b, _)

    a, _, _ = (1, 2, 3)
    print(a, _)

    _, a, _ = (1, 2, 3)
    print(a, _)

    _, _, a = (1, 2, 3)
    print(a, _)

if __name__ == "__main__":
    main()