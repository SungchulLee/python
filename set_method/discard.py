def main():
    s = {1,2,3,4,5,3,4,5}
    print(s)

    s.discard(5)
    print(s)

    s.discard(7)
    print(s)

if __name__ == "__main__":
    main()