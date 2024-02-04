from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

def main():
    color_1 = Color(51, 155, 255) 
    color_2 = Color(52, 155, 255) 
    color_3 = Color(53, 155, 255) 
    color_4 = Color(54, 155, 255) 

    print(color_4[0])  # 네임드투플은 투플처럼 사용할 수 있다.
    print(color_4.red) # 네임드투플은 클래스처럼 사용할 수 있다.

if __name__ == "__main__":
    main()