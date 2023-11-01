import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    array = []
    sum_row = []
    sum_col = []
    inl = []
    inr = []
    for i in range(100):
        array.append(list(map(int, input().split())))
        sum_row.append(sum(array[i]))
        inl.append(array[i][i])
        inr.append(array[i][-(i+1)])
    for i in range(100):
        sum_col.append(sum([a[i] for a in array]))
    sum_inl = sum(inl)
    sum_inr = sum(inr)
    max_row = max(sum_row)
    max_col = max(sum_col)
    result = max(max_row, max_col, sum_inl, sum_inr)
    print(f'#{tc} {result}')