def my_own_range(start, end, step_size=1):
    current_state = start
    while current_state < end:
        yield current_state
        current_state += step_size

def main():
    for i in range(1,10,2):
        print(i, end=" ")
    print()

    for i in my_own_range(1,10,2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()