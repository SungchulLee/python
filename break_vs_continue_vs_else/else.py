def main():
    for i in range(4): 
        print(i)
        if i == 2:
            break
        print(f'current i : {i}')
    else: # if break does not work
        print("this line works only when break does not work")

    for i in range(4): 
        print(i)
        if i == 10:
            break
        print(f'current i : {i}')
    else: # if break does not work
        print("this line works only when break does not work")

if __name__ == "__main__":
    main()