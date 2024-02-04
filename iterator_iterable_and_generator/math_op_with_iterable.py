def main():
    a = []
    for i in range(1,101):
        a.append(i)
    print(a)

    print(max(a))
    print(min(a))
    print(sum(a))
    print(len(a))
    print('Average : ', sum(a) / len(a))

if __name__ == "__main__":
    main()