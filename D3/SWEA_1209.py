import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    array = []
    sum_row = []
    sum_col = []
    # 왼쪽위에서부터 내려가는 대각선 값들 입력
    inl = []
    # 오른쪽위에서부터 내려가는 대각선 값들 입력
    inr = []
    for i in range(100):
        array.append(list(map(int, input().split())))
        # 행 입력받을때마다 바로바로 합 구해주기
        sum_row.append(sum(array[i]))
        # 왼쪽 맨위에서부터 한칸 내려오면 오른쪽 한칸 가면서 대각선 값들 넣어주기
        inl.append(array[i][i])
        # 오른쪽 맨위에서부터 한칸 내려오면 왼쪽 한칸 가면서 대각선 값들 넣어주기
        inr.append(array[i][-(i+1)])
    for i in range(100):
        # 열 추출해서 더해서 넣어주기
        sum_col.append(sum([a[i] for a in array]))
    sum_inl = sum(inl)
    sum_inr = sum(inr)
    max_row = max(sum_row)
    max_col = max(sum_col)
    # 행 합, 열 합, 대각선 합 중에서 가장 큰 값 구하기
    result = max(max_row, max_col, sum_inl, sum_inr)
    print(f'#{tc} {result}')
