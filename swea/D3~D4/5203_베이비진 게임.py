import sys
sys.stdin = open("input.txt", "r")
'''
    문제가 약간 잘못됐다고 생각함..
    둘 다 동시에 triplet이나 run이 되었을 때, 무승부로 되야하지만
    여기서는 무조건 player1이 이기도록 해야 함.
'''
T = int(input())

def triplet(player: list) -> bool:
    if max(player) >= 3:
        return True
    else:
        return False

def run_(player: list) -> bool:
    for i in range(0, 8):
        if player[i] and player[i+1] and player[i+2]:
            return True
    return False

def winner() -> int:
    draw = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    L = len(draw)
    for i in range(L):
        if i % 2:
            player2[draw[i]] += 1
            result_2 = triplet(player2) or run_(player2)
            if result_2:
                return 2
        else:
            player1[draw[i]] += 1
            result_1 = triplet(player1) or run_(player1)
            if result_1:
                return 1

    return 0


for tc in range(1, T+1):
    print('#{} {}'.format(tc, winner()))


