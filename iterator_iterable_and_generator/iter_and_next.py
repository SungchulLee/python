def main():
    # load iterators fully
    obj0 = [1, 2, 3] # iterable
    obj1 = iter(obj0) # iterator
    obj2 = obj0.__iter__() # iterator

    # looping the fully loaded iterators
    while True:
        try:
            a_from_obj1 = next(obj1)
            a_from_obj2 = next(obj2)
            print(f"{a_from_obj1 = }, {a_from_obj2 = }")
        except StopIteration:
            print("Built-in Exception StopIteration Occurs!")
            print("I will break the while loop!")
            break
    print("I am out of the while loop!")

    # looping empty loaded iterators
    while True:
        try:
            a_from_obj1 = obj1.__next__()
            a_from_obj2 = obj2.__next__()
            print(f"{a_from_obj1 = }, {a_from_obj2 = }")
        except StopIteration:
            print("Built-in Exception StopIteration Occurs!")
            print("I will break the while loop!")
            break
    print("I am out of the while loop!")

    # load iterators fully, again
    obj0 = [1, 2, 3] # iterable
    obj1 = iter(obj0) # iterator
    obj2 = obj0.__iter__() # iterator

    # looping the fully loaded iterators
    while True:
        try:
            a_from_obj1 = obj1.__next__()
            a_from_obj2 = obj2.__next__()
            print(f"{a_from_obj1 = }, {a_from_obj2 = }")
        except StopIteration:
            print("Built-in Exception StopIteration Occurs!")
            print("I will break the while loop!")
            break
    print("I am out of the while loop!")

if __name__ == "__main__":
    main()