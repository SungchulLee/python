def main():
    x = {'pork':25.3, 'beef':33.8, 'chicken':22.7, 'horse': 33.3}
    print(x)

    del x['horse']
    print(x)

if __name__ == "__main__":
    main()