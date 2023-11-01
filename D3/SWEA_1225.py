import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 테스트케이스 숫자 입력
    tc = int(input())
    queue = list(map(int,input().split()))
    
    # 가장 작은 수 기준으로 15로 나눠서 계산량 줄여줌. 한 사이클이 15
    target = min(queue)
    count = target // 15
    count -= 1 # 한사이클 전까지만 적용해줌. 끝까지 사이클 돌려서 적용했더니 다른 수가 먼저 0이 되는 경우도 있었어서..

    n_queue = []
    # 사이클 여러번 돌린 후의 작아진 값들로 새로운 리스트 생성
    for i in queue:
        n_queue.append(i - count*15)
    # 일단 큰 수로 for문 돌려줌. 중간에 숫자 하나라도 0 이하가 되면 바로 break해줄거라서
    for i in range(int(1e9)):
        # 가장 앞에 수 빼서 사이클 규칙 적용 후 맨 뒤에 넣어줌
        value = n_queue.pop(0)
        value -= (i % 5 + 1)
        if value > 0:
            n_queue.append(value)
        else: # 숫자 하나라도 0이 되는 순간의 리스트가 비밀번호임
            value = 0
            n_queue.append(value)
            break
    print(f'#{tc} ', end='')
    for item in n_queue:
        print(item, end=' ')
    print()