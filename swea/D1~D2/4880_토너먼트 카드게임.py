import sys
sys.stdin = open("input.txt", "r")
'''
    이진 분할 문제 - 트리로도 해결할 수 있을듯
    - 당시에 어려워서 못풀고 현승님 코드를 보면서 배웠다.
    - 하지만, 다시 풀어보니 생각보다 훨씬 쉽게 풀 수 있었다.
    - 만약 다르게 푼다면 트리 형식으로 이기면 한명을 부모 노드에 올리고
    - 지면 0으로 초기화하는 방법도 좋을 것 같다.
    
    이후 공부 방향
    - 아직까지도 재귀로 해봐! 하면 시간이 걸려서 할 수는 있지만 버벅거리는 게 사실이다.
    - 매번 재귀를 풀 때마다 어떻게 될지 생각하지만 생각한 방향으로 전혀 동작하지 않을 때도 있다.
    - 따라서, 조금 더 완벽하게 이해하고 내가 생각한 바가 그대로 구현될 수 있도록 노력해야겠다.
    - 문제를 해결할 때, 재귀로 코드를 변경해보고 미리 테스트를 돌리지 말고 완벽하게 되는지 생각한 후 해보자.
        
    
    
    
    1. 두명 또는 한명이 될 때까지 이진 분할.
    2. 분할이 완료되면 두명일 때에는 싸워서 승자를 보내고, 한명일 때에는 바로 return
    3. 그러면 다시 그 승자들을 재귀적으로 싸움에 붙임.
    4. 그럼 결국 마지막 승자만 남음.
'''

def battle(idx1, idx2):
    if weapon[idx1] == weapon[idx2]:
        return idx1
    else:
        if weapon[idx1] == 1:
            if weapon[idx2] == 2:
                return idx2
            elif weapon[idx2] ==3:
                return idx1
        elif weapon[idx1] == 2:
            if weapon[idx2] == 1:
                return idx1
            elif weapon[idx2] == 3:
                return idx2
        elif weapon[idx1] == 3:
            if weapon[idx2] == 1:
                return idx2
            elif weapon[idx2] == 2:
                return idx1


def tournament(start, end):
    if start + 1 == end:
        return battle(start, end)
    elif start == end:
        return start
    else:
        pivot = (start + end) // 2
        return battle(tournament(start, pivot), tournament(pivot+1, end))


# 1은 가위, 2는 바위, 3은 보
for tc in range(1, int(input())+1):
    N = int(input())
    weapon = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(1, N)))