class MyOwnRange:
    
    def __init__(self, start, end, step_size):
        self.current_state = start 
        self.end = end             
        self.step_size = step_size 

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_state >= self.end:
            raise StopIteration('Built-in Exception StopIteration Occurs!')
        current_state = self.current_state
        self.current_state += self.step_size 
        return current_state 

def main():
    for i in range(1,10,2):
        print(i, end=" ")
    print()

    for i in MyOwnRange(1,10,2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()