def main():
    x = {'pork':25.3, 'beef':33.8, 'chicken':22.7, 'horse': 33.3}
    popped_item = x.pop('horse')
    print(x)
    print(popped_item)


if __name__ == "__main__":
    main()