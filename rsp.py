import random


def one_player_turn():
    while True:
        player = input("가위, 바위, 보 중 하나를 내세요! : ")
        if player in ['가위', '바위', '보']:
            return player
        else:
            print("잘못된 입력입니다! 가위, 바위, 보 중 하나를 선택해주세요.")


def two_computer_turn():
    choices = ['가위', '바위', '보']
    return random.choice(choices)


def winner(player, computer):
    if player == computer:
        return "무승부!"
    elif (player == '가위' and computer == '보') or \
            (player == '보' and computer == '바위') or \
            (player == '바위' and computer == '가위'):
        return "플레이어 승리!"
    else:
        return "컴퓨터 승리!"


def main():
    while True:
        player = one_player_turn()
        computer = two_computer_turn()

        print("플레이어의 선택:", player)
        print("컴퓨터의 선택:", computer)

        result = winner(player, computer)
        print("결과 :", result)

        play_again = input("게임을 다시 하시겠습니까? ('네'/'아니오'): ")
        if play_again != '네':
            print('게임이 종료되었습니다.')
            break


if __name__ == "__main__":
    main()
