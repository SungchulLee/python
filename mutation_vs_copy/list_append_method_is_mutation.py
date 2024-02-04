def main():
    a = []
    for i in range(100):
        a.append(i)
        print(f"{id(a) = }")

if __name__ == "__main__":
    main()

