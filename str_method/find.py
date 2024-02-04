def main():
    message = 'Hello World!'
    print(message.find('Hello')) # report the first index where sub-string starts
    print(message.find('l')) # report the first index where sub-string starts
    print(message.find('Universe')) # -1 means there is no such such sub-string

if __name__ == "__main__":
    main()
