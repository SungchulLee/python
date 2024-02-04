def main():
    # Example 1: Convert and print the message in uppercase without changing the original
    message = 'Hello World!'
    print(message.upper())  # Print the message in uppercase
    print(message)  # Print the original message (unchanged) since string is immutable

    # Example 2: Create a new variable with the message in uppercase and print both
    message = 'Hello World!'
    new_message = message.upper()  # Create a new variable with the message in uppercase
    print(new_message)  # Print the new message in uppercase
    print(message)  # Print the original message (unchanged)

if __name__ == "__main__":
    main()
