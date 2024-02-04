obj0 = [1, 2, 3]

def main():
    obj1 = set(i**2 for i in obj0) # set comprehension
    print(f"{obj1 = }")

if __name__ == "__main__":
    main()