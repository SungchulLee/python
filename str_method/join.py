def main():
    Courses = ['History', 'Math', 'Physics', 'CompSci']

    joined_string = ' '.join(Courses)
    print(joined_string)

    joined_string = ', '.join(Courses)
    print(joined_string)

    joined_string = ' - '.join(Courses)
    print(joined_string)

    joined_string = '-'.join(Courses)
    print(joined_string)

    joined_string = ' * '.join(Courses)
    print(joined_string)

    joined_string = '*'.join(Courses)
    print(joined_string)

if __name__ == "__main__":
    main()
