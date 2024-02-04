def main():
    # Printing boolean values of various falsy values
    print(bool(0))      # False, as 0 is considered falsy
    print(bool(None))   # False, as None is considered falsy
    print(bool(''))     # False, as an empty string is considered falsy
    print(bool([]))     # False, as an empty list is considered falsy
    print(bool({}))     # False, as an empty dictionary is considered falsy

    # Printing boolean values of various truthy values
    print(bool(2))      # True, as non-zero integers are considered truthy
    print(bool('two'))  # True, as non-empty strings are considered truthy
    print(bool([2]))    # True, as non-empty lists are considered truthy

if __name__ == "__main__":
    main()