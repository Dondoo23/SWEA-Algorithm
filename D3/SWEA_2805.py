import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    profit = []
    for i in range(n):
        # 공백없이 주어진 숫자를 분할하여 정수리스트로 입력
        profit.append(list(map(int,input())))
        
    mid = n // 2 # 5 / 2 = 2 -> 01234 에서 가운데 인덱스
    sum = 0
    for i in range(n):
        # 0-2=2 1-2=1 2-2=0 3-2=1 4-2=2 -> cal = 2 1 0 1 2 식으로 나온다
        cal = abs(i-mid)
        # 앞에서 cal만큼 띄우고 뒤에서 cal만큼 뛰어서 그 사이 값들만 더함
        for j in range(cal, n-cal):
            sum += profit[i][j]

    print(f'#{test_case} {sum}')