import numpy as np

def main():
    a = 'HI DO'

    title0 = 'Character'
    title1 = '(Positive) Index'
    title2 = 'Negative Index'
    print(f'{title0:20} {a[0]:5} {a[1]:5} {a[2]:5} {a[3]:5} {a[4]:5}')
    print(f'{title1:20} {0:<5} {1:<5} {2:<5} {3:<5} {4:<5}')
    print(f'{title2:19} {-5:<5} {-4:<5} {-3:<5} {-2:<5} {-1:<5}')

if __name__ == "__main__":
    main()