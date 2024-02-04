def main():
    s = {3,5,3,5,3,5}
    print(s)

    s.update([3,7,8])
    print(s)

    s.update({30,70,80,70,70,80})
    print(s)

if __name__ == "__main__":
    main()