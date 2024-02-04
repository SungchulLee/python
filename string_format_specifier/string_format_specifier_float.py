import numpy as np

def main():
    i = np.pi

    sentence = 'The value is {}'.format(i)
    print(sentence)

    sentence = 'The value is {:.4f}'.format(i)
    print(sentence)

    sentence = 'The value is {:10.4f}'.format(i)
    print(sentence)

    sentence = 'The value is {:010.4f}'.format(i)
    print(sentence)

    sentence = 'The value is {:<10.4f}'.format(i)
    print(sentence)

    sentence = 'The value is {:.4%}'.format(i)
    print(sentence)

if __name__ == "__main__":
    main()