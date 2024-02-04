def main():
    a = [1,2,3]
    print(f"{id(a) = }")

    # inplace list concatenation is mutation
    a += [4,5,6]
    print(f"{id(a) = }")

    # list concatenation is not mutation, it is copy
    a = a + [7,8,9]
    print(f"{id(a) = }")

if __name__ == "__main__":
    main()

