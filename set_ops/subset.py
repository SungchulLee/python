def main():
    A = {1,2,3,4,5}
    B = {4,5}
    print(A<=B)   
    print(A<B)    

    A = {1,2,3,4,5}
    B = {1,2,3,4,5}
    print(A<=B)   
    print(A<B)   

    A = {4,5}
    B = {1,2,3,4,5}
    print(A<=B)    
    print(A<B)    

if __name__ == "__main__":
    main()