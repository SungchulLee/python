from collections import deque

def main():
    lst = [0,1,2,3,4,5,6,7,8,9] 
    print(lst) 
    print(lst[0]) 
    print(lst[-1]) 
    print(lst[2:5])

    lst = deque([0,1,2,3,4,5,6,7,8,9])
    print(lst) 
    print(lst[0]) 
    print(lst[-1]) 
    try:
        print(lst[2:5])
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()