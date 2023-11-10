import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, Q = map(int,input().split()) # N개의 상자, Q번 수행
    arr = [0] * N
    for i in range(Q):
        L, R = map(int, input().split()) # 1, 3
        L -= 1
        for j in range(L, R):
            arr[j] = i+1
    print(f'#{test_case} ', end='')
    print(*arr)