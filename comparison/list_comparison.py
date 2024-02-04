def main():
    print([0, 1, 2] < [5, 1, 2])                  # True
    print([0, 1, 2000000000] < [0, 1, 2])         # False
    print(['Jones', 'Sally'] < ['Jones', 'Fred']) # False
    print(['Jones', 'Sally'] > ['Adams', 'Sam'])  # True

if __name__ == "__main__":
    main()