def main():
    inventory = {'apple': 10, 'grape': 20, 'banana': 30}

    # Example 1: Check if 'apple' is a key in the inventory dictionary
    print('apple' in inventory)  # Check if 'apple' is a key in the dictionary (True)
    print('apple' not in inventory)  # Check if 'apple' is not a key in the dictionary (False)

    # Example 2: Check if the value 10 is present in the inventory dictionary (as a key)
    # Note that the dict membership checks only keys, not values
    print(10 in inventory)  # Check if the value 10 is a key in the dictionary (False)
    print(10 not in inventory)  # Check if the value 10 is not a key in the dictionary (True)

if __name__ == "__main__":
    main()
