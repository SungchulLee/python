def main():
    # Example 1: Convert and print the message in capitalizecase without changing the original
    message = 'Hello World!'
    print(message.capitalize())  # Print the message in capitalizecase
    print(message)  # Print the original message (unchanged) since string is immutable

    # Example 2: Create a new variable with the message in capitalizecase and print both
    message = 'Hello World!'
    new_message = message.capitalize()  # Create a new variable with the message in capitalizecase
    print(new_message)  # Print the new message in capitalizecase
    print(message)  # Print the original message (unchanged)

if __name__ == "__main__":
    main()
