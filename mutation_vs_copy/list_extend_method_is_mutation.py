def main():
    a = [1,2,3]
    print(f"{id(a) = }, {a = }")

    a.extend([4,5,6])
    print(f"{id(a) = }, {a = }")

if __name__ == "__main__":
    main()

