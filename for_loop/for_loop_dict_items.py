def main():
    for a in {'one' : 1, 'two' : 2, 'three' : 3}.items():
        print(a, type(a))

    for a0, a1 in {'one' : 1, 'two' : 2, 'three' : 3}.items():
        print(a0, a1)

    for a0, _ in {'one' : 1, 'two' : 2, 'three' : 3}.items():
        print(a0)

if __name__ == "__main__":
    main()