import copy

def main():
    a = [0,1,2] 
    b = copy.copy(a)
    print(f"{a = }, {b = }")

    a[0] = "zero"
    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()

