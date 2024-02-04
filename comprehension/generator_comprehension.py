obj0 = [1, 2, 3]

def main():
    obj2 = [i**2 for i in obj0] # list comprehension
    print(f"{obj2 = }")

    obj3 = (i**2 for i in obj0) # generator comprehension
    print(f"{obj3 = }")

    for i in obj3:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()