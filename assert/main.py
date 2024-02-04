
def main():
    a = 1.3
    b = 1.3

    # Assertions are simply boolean expressions that 
    # checks if the conditions return true or not. 
    # If it is true, the program does nothing 
    # and move to the next line of code. 
    # However, if it's false, the program stops and throws an error.
    # It is also a debugging tool as it brings the program on halt 
    # as soon as any error is occurred 
    # and shows on which point of the program error has occurred.
    assert(type(a) is int) # AssertionError

    c = a + b 
    print(a == b)

if __name__ == "__main__":
    main()