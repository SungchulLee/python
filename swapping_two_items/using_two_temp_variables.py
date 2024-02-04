def main():
    a = 1
    b = 2

    temp_a = a 
    temp_b = b

    a = temp_b
    b = temp_a

    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()