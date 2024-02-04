def main():
    a = {'Calculus', 'Algebra'} 
    b = a
    print(f"{a = }, {b = }")

    a.remove('Calculus')
    print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()

