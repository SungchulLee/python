def main():
    s = {3,5,3,5,3,5}
    print(s, type(s))

    s = set([3,5,3,5,3,5])
    print(s, type(s))

    s = {} # this is an empty dict
    print(s, type(s))

    s = set() # this is an empty set
    print(s, type(s))

if __name__ == "__main__":
    main()