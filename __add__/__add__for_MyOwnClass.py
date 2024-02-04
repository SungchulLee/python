class OnePlusOne:
    def __add__(self, other):
        return '일 더하기 일은 귀요미'
        
        
def main():
    a = OnePlusOne()
    b = OnePlusOne()
    c1 = a + b
    c2 = OnePlusOne.__add__(a, b)
    c3 = a.__add__(b)
    print(c1)
    print(c2)
    print(c3)

if __name__ == "__main__":
    main()