import copy 

def main():
    a = [0,1,2,[3,4,5]] 
    b = a.copy()
    c = copy.deepcopy(a)
    print(f"{a = }, {b = }, {c = }")

    a[-1][0] = "three"
    print(f"{a = }, {b = }, {c = }")

if __name__ == "__main__":
    main()

