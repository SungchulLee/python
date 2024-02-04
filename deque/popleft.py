from collections import deque

def main():
    lst = []
    for i in range(5):
        lst.append(i)
        print(lst)
    for _ in range(5):
        lst.pop(0)
        print(lst)

    lst = deque()
    for i in range(5):
        lst.append(i)
        print(lst)
    for _ in range(5):
        lst.popleft()
        print(lst)

if __name__ == "__main__":
    main()