def main():
    for i in range(4): 
        print(i)
        if i == 2:
            continue
        print(f'current i : {i}')

if __name__ == "__main__":
    main()