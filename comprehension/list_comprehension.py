obj0 = [1, 2, 3]

def main():
    obj1 = []
    for i in obj0:
        obj1.append(i**2)
    print(f"{obj1 = }")

    obj2 = [i**2 for i in obj0]
    print(f"{obj2 = }")

if __name__ == "__main__":
    main()