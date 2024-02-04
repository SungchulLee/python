def main():
    # First loop using integer 0 to 4
    x = 0
    while True:
        if x == 5:
            break
        print(x)
        x += 1

    # Second loop using upcasting: integer 0 to 4, 1 is upcasted to True
    x = 0
    while 1:  # 1 is upcasted to True
        if x == 5:
            break
        print(x)
        x += 1

if __name__ == "__main__":
    main()
