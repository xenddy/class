import random


def updown_game():
    random_number = random.randint(1, 100)
    score = 0
    best_score = float('inf')

    while True:
        guess = input("숫자를 입력해 주세요! (1~100까지)")

        if guess.isdigit():
            break
        else:
            print("숫자가 아닙니다. 숫자로만 입력해 주세요!")

        guess = int(guess)  # input으로 받은 값을 string에서 int로 바꾸기

        if guess < 1 or guess > 100:
            print("1부터 100까지의 숫자만 입력할 수 있습니다.")

        score += 1  # 시도 횟수 1회씩 추가

        if guess < random_number:
            print("업!")
        elif guess > random_number:
            print("다운!")
        else:
            print(f"정답! {score}번 만에 맞추셨어요!")
            if score < best_score:
                best_score = score
                print("축하합니다! 최고 기록을 갱신했어요!")
            else:
                print(f"최고 기록은 현재 {best_score}번 입니다.")
            break

    return best_score


def start():
    print("*** 업 다운 게임 ***")
    best_score = float('inf')  # 시도 횟수를 무한대로 설정

    while True:
        best_score = min(best_score, updown_game())
        play_again = input("게임을 다시 하시겠습니까? (yes/no): ")
        if play_again.lower() != 'yes':
            print("게임 종료")
            print(f"최고 시도 횟수: {best_score}")
            break


if __name__ == "__main__":
    start()
