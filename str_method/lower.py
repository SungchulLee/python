def main():
    # Example 1: Convert and print the message in lowercase without changing the original
    message = 'Hello World!'
    print(message.lower())  # Print the message in lowercase
    print(message)  # Print the original message (unchanged) since string is immutable

    # Example 2: Create a new variable with the message in lowercase and print both
    message = 'Hello World!'
    new_message = message.lower()  # Create a new variable with the message in lowercase
    print(new_message)  # Print the new message in lowercase
    print(message)  # Print the original message (unchanged)

if __name__ == "__main__":
    main()
