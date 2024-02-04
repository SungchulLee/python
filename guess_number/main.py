import random

def main():
    given_n = random.randint(1, 100) # 100이 포함됨
    num_tries = 10

    for i in range(1, num_tries+1):
        your_guess = int(input('1과 100사이의 숫자를 입력해 주세요.'))
        if given_n == your_guess: 
            print('축하합니다. 맟추셨네요.')
            break
        elif given_n > your_guess:
            if i != num_tries: 
                print('숫자가 너무 작군요. 숫자를 키워보세요.')
        else:
            if i != num_tries: 
                print('숫자가 너무 크군요. 숫자를 줄여보세요.')
    else: # no break
        print(f'아쉽군요. {i}번 추측하셨는 모두 실패하셨군요.')
                
    print(f'주어진 숫자 : {given_n}')
    print(f'당신의 최종 추측 : {your_guess}')

if __name__ == "__main__":
    main()