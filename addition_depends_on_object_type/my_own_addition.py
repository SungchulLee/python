class One_Plus_One:
    
    def __init__(self, string):
        self.string = string
        
    def __add__(self, other):
        if (self.string=='1') and (other.string=='1'):
            return '일더하기 일은 귀요미'
        
        
def main():
    a = One_Plus_One("1")
    b = One_Plus_One("1")
    c = a + b

    print(f"{c = }")

if __name__ == "__main__":
    main()