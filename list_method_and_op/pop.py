def main():
    # Example 0: Pop the last item from the list and print the updated list
    x = ['History', 'Math', 'Physics', 'CompSci', 'Math']
    x.pop()  # Remove the last item from the list
    print(x)

    # Example 1: Pop elements from the end of the list and print the updated list
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(10):
        x.pop()  # Remove the last element from the list
        print(x)

    # Example 2: Pop elements from the end of the list, store the popped element, and print both
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(10):
        item = x.pop()  # Remove the last element from the list and store it in 'item'
        print(item, x)

    # Example 3: Pop elements from the beginning of the list, store the popped element, and print both
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(10):
        item = x.pop(0)  # Remove the first element from the list and store it in 'item'
        print(item, x)

if __name__ == "__main__":
    main()

