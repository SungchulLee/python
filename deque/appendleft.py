from collections import deque

def main():
    # lst = []
    # for i in range(5):
    #     lst.append(i)
    #     print(lst)

    lst = deque()
    for i in range(5):
        lst.appendleft(i)
        print(lst)

if __name__ == "__main__":
    main()