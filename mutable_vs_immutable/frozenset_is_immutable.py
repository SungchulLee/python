def main():
    a = frozenset([1,2,3,1,2,3,1,2])

    # We cannot perform add, update or remove operations on frozensets 
    # because they are immutable
    try:
        a.add(10)
        print(f"{a = }")
    except AttributeError as e:
        print(e)

if __name__ == "__main__":
    main()

