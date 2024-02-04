def fizz_buzz_response(i):
    
    """
    if i can be divided by 3 but not by 5, return 'Fizz'
    if i can be divided by 5 but not by 3, return 'Buzz'
    if i can be divided by both 3 and 5, return 'FizzBuzz'
    if i cannot be divided by either 3 or 5, return str(i) 
    """
    
    if i % 15 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0: 
        return 'Fizz'
    elif i % 5 == 0: 
        return 'Buzz'
    else:
        return i

def main():
    for i in range(1, 101):
        print(fizz_buzz_response(i), end='\t') 

if __name__ == "__main__":
    main()