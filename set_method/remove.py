def main():
    s = {1,2,3,4,5,3,4,5}
    print(s)

    s.remove(5)
    print(s)

    try:
        s.remove(7)
        print(s)
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()