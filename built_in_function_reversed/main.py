def main():
    x = [1,5,3,4,2]
    x = reversed([1,5,3,4,2])
    print(x)
    x = list(reversed([1,5,3,4,2]))
    print(x)

    x = "Hello World"
    for i in reversed("Hello World"):
        print(i, end="\t")


if __name__ == "__main__":
    main()