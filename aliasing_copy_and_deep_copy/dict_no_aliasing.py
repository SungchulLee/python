def main():
    a = {"zero":0,"one":1,"two":2}
    b = {"zero":0,"one":1,"two":2}
    print(f"{a = }, {b = }")

    a["zero"] = "ZERO"
    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()

