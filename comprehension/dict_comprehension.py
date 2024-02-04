names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

def main():
    my_dict = {}
    for name, hero in zip(names, heros):
        my_dict[name] = hero
    print(my_dict)

    my_dict = {name: hero for name, hero in zip(names, heros)}
    print(my_dict)

if __name__ == "__main__":
    main()