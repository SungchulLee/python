def main():
    for i in range(1,10,2):
        print(i, end=" ")
    print()

    my_own_range = ( 2 * n + 1 for n in range(5) )
    for i in my_own_range:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()