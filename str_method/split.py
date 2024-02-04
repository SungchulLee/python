def main():
    Courses = ['History', 'Math', 'Physics', 'CompSci']

    joined_string = ' '.join(Courses)
    print(joined_string)
    lst = joined_string.split()
    print(lst)

    joined_string = ', '.join(Courses)
    print(joined_string)
    lst = joined_string.split(', ')
    print(lst)

    joined_string = ' - '.join(Courses)
    print(joined_string)
    lst = joined_string.split(' - ')
    print(lst)

    joined_string = '-'.join(Courses)
    print(joined_string)
    lst = joined_string.split('-')
    print(lst)

    joined_string = ' * '.join(Courses)
    print(joined_string)
    lst = joined_string.split(' * ')
    print(lst)

    joined_string = '*'.join(Courses)
    print(joined_string)
    lst = joined_string.split('*')
    print(lst)

if __name__ == "__main__":
    main()
