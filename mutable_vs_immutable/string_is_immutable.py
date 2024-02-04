def main():
    a = "Hellow World"

    try:
        a[1] = "E"
        print(f"{a = }")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()

