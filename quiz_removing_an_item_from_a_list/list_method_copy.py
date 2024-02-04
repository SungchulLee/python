def main():
    a = [1,2,3,4]
    b = [1,2,5,6]

    for item in a.copy(): 
        if item in b:
            a.remove(item)
            
    print(a)

if __name__ == "__main__":
    main()