def main():
    a = {"zero": 0, "one": 1, "two": 2}
    a["three"] = 3
    a["zero"] = "ZERO"
    print(f"{a = }")

if __name__ == "__main__":
    main()

