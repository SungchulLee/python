import copy 

def main():
    a = [0,1,2] 
    b = a 
    c = [0,1,2]
    print(a is b, a is c)
    print(f"{id(a) = }, {id(b) = }, {id(c) = }")

if __name__ == "__main__":
    main()

