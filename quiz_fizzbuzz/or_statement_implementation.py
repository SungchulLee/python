def fizz_buzz_response(i):
    
    """
    if i can be divided by 3 but not by 5, return 'Fizz'
    if i can be divided by 5 but not by 3, return 'Buzz'
    if i can be divided by both 3 and 5, return 'FizzBuzz'
    if i cannot be divided by either 3 or 5, return str(i) 
    """
    
    return 'Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i

def main():
    for i in range(1, 101):
        print(fizz_buzz_response(i), end='\t') 

if __name__ == "__main__":
    main()