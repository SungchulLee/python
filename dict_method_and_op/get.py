def main():
    x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}

    print(x['pork'])  # Output: 25.3
    print(x.get('pork'))  # Output: 25.3

    # Accessing a non-existent key using square brackets (throws an error)
    # print(x['horse'])  # Uncommenting this line would raise a KeyError

    # Accessing a non-existent key using the get method (returns None)
    print(x.get('horse'))  # Output: None

    # Accessing a non-existent key using the get method with a default value
    print(x.get('horse', 'Not_Available'))  # Output: Not_Available

if __name__ == "__main__":
    main()
