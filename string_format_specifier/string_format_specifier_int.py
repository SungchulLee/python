
def main():
    i = 1000**3

    sentence = 'The value is {}'.format(i)
    print(sentence)

    sentence = 'The value is {:20}'.format(i)
    print(sentence)

    sentence = 'The value is {:020}'.format(i)
    print(sentence)

    sentence = 'The value is {:<20}'.format(i)
    print(sentence)

    sentence = 'The value is {:,}'.format(i)
    print(sentence)

if __name__ == "__main__":
    main()