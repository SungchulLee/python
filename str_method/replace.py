def main():
    # Example 1: Convert and print the replaced message without changing the original
    message = 'Hello World!'
    print(message.replace('World', 'Universe'))  # Print the replaced message
    print(message)  # Print the original message (unchanged) since string is immutable

    # Example 2: Create a new variable with the replaced message and print both
    message = 'Hello World!'
    new_message = message.replace('World', 'Universe')  # Create a new variable with the replaced message
    print(new_message)  # Print the replaced message
    print(message)  # Print the original message (unchanged)

if __name__ == "__main__":
    main()
