def main():
    a = [0,1,2,[3,4,5]] 
    b = a.copy()
    print(f"{a = }, {b = }")

    a[-1][0] = "three"
    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()

