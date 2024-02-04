def main():
    for i in range(1, 101):
        if i % 3 == 0: 
            print('Fizz', end='\t')
        elif i % 5 == 0: 
            print('Buzz', end='\t')
        elif i % 15 == 0:
            print('FizzBuzz', end='\t')
        else:
            print(str(i), end='\t')

if __name__ == "__main__":
    main()