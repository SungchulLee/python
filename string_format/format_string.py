def main():
    name = 'Ariel'
    age = 26
    print("My name is {} and I am {} years old.".format(name, age)) 
    print("My name is {0} and I am {1} years old.".format(name, age))
    print("My name is {1} and I am {0} years old.".format(age, name))

if __name__ == "__main__":
    main()