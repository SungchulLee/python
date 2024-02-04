obj0 = {'one' : 1, 'two' : 2, 'three' : 3}.items()
obj1 = iter(obj0)
obj2 = obj0.__iter__()

def main():
    for a in obj0:
        print(a, end=" ")
    print()

    for a in obj1:
        print(a, end=" ")
    print()

    for a in obj2:
        print(a, end=" ")
    print()

    # '__iter__' in dir(obj0) = True '__next__' in dir(obj0) = False
    # this means num0 is iterable
    print(f"{'__iter__' in dir(obj0) = }", f"{'__next__' in dir(obj0) = }")

    # '__iter__' in dir(obj1) = True '__next__' in dir(obj1) = True
    # this means num1 is an iterator
    print(f"{'__iter__' in dir(obj1) = }", f"{'__next__' in dir(obj1) = }")

    # '__iter__' in dir(obj2) = True '__next__' in dir(obj2) = True
    # this means num2 is an iterator
    print(f"{'__iter__' in dir(obj2) = }", f"{'__next__' in dir(obj2) = }")

if __name__ == "__main__":
    main()