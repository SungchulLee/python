import datetime

def main():
    t = datetime.datetime(2016, 9, 24, 12, 30, 45)

    print(t)
    print('{:%B %d, %Y}'.format(t))
    print('{:%Y/%b/%d}'.format(t))

if __name__ == "__main__":
    main()